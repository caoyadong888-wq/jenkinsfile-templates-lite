#!/usr/bin/env python3
"""Structural checks for Declarative Jenkinsfiles.

This does not start Jenkins and does not parse full Groovy. It balances
braces outside strings and comments, then looks for directive words and
parameter names. Check upstream docs for semantics on your controller.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PROFILE_RE = re.compile(r"pack-profile:\s*(simple|docker|matrix)\b")
PARAM_RE = re.compile(
    r"\b(?:string|choice|booleanParam|text)\s*\(\s*name:\s*'([A-Za-z_][A-Za-z0-9_]*)'"
)
VOCAB = (
    "agent",
    "axes",
    "axis",
    "docker",
    "environment",
    "matrix",
    "options",
    "parameters",
    "pipeline",
    "post",
    "stage",
    "stages",
    "steps",
    "when",
)
ALWAYS = ("pipeline", "agent", "parameters", "stages", "stage", "steps")
EXTRA = {
    "simple": (),
    "docker": ("docker",),
    "matrix": ("matrix", "axes", "axis"),
}


def scan(text: str) -> tuple[str, str | None]:
    """Return code with strings and comments removed, or an error."""
    i = 0
    n = len(text)
    out: list[str] = []
    depth = 0
    line = 1
    while i < n:
        char = text[i]
        nxt = text[i + 1] if i + 1 < n else ""
        if char == "/" and nxt == "/":
            i += 2
            while i < n and text[i] != "\n":
                i += 1
            continue
        if char == "/" and nxt == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                if text[i] == "\n":
                    out.append("\n")
                    line += 1
                i += 1
            if i + 1 >= n:
                return "", f"unclosed block comment at line {line}"
            i += 2
            continue
        if text.startswith("'''", i) or text.startswith('"""', i):
            quote = text[i : i + 3]
            i += 3
            closed = False
            while i < n:
                if text.startswith(quote, i):
                    i += 3
                    closed = True
                    break
                if text[i] == "\n":
                    out.append("\n")
                    line += 1
                i += 1
            if not closed:
                return "", f"unclosed triple quote at line {line}"
            out.append("''")
            continue
        if char in ("'", '"'):
            quote = char
            i += 1
            closed = False
            while i < n:
                if text[i] == "\\":
                    i += 2
                    continue
                if text[i] == "\n":
                    out.append("\n")
                    line += 1
                    i += 1
                    continue
                if text[i] == quote:
                    i += 1
                    closed = True
                    break
                i += 1
            if not closed:
                return "", f"unclosed string at line {line}"
            out.append("''")
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                return "", f"extra closing brace at line {line}"
        if char == "\n":
            line += 1
        out.append(char)
        i += 1
    if depth != 0:
        return "", f"unbalanced braces, depth {depth}"
    return "".join(out), None


def has_word(code: str, word: str) -> bool:
    return re.search(rf"\b{re.escape(word)}\b", code) is not None


def check_text(path_label: str, text: str) -> tuple[bool, str]:
    lines: list[str] = [f"check: {path_label}"]
    profile_match = PROFILE_RE.search(text)
    if profile_match is None:
        lines.append("profile: missing")
        lines.append("file_result: fail")
        return False, "\n".join(lines) + "\n"
    profile = profile_match.group(1)
    lines.append(f"profile: {profile}")
    code, error = scan(text)
    if error is not None:
        lines.append(f"braces: {error}")
        lines.append("file_result: fail")
        return False, "\n".join(lines) + "\n"
    lines.append("braces: balanced")
    present = [word for word in VOCAB if has_word(code, word)]
    lines.append("directives: " + " ".join(present))
    names = sorted(set(PARAM_RE.findall(text)))
    lines.append("parameters: " + (" ".join(names) if names else "(none)"))
    missing = [word for word in (*ALWAYS, *EXTRA[profile]) if word not in present]
    if not names:
        missing.append("parameters-name")
    if missing:
        lines.append("missing: " + " ".join(missing))
        lines.append("file_result: fail")
        return False, "\n".join(lines) + "\n"
    lines.append("file_result: ok")
    return True, "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: check_jenkinsfile.py JENKINSFILE...", file=sys.stderr)
        return 2
    failed = 0
    chunks: list[str] = []
    for arg in argv:
        path = Path(arg)
        if not path.is_file():
            chunks.append(f"check: {arg}\nprofile: missing\nfile_result: fail\n")
            failed += 1
            continue
        text = path.read_text(encoding="utf-8")
        ok, block = check_text(arg, text)
        chunks.append(block)
        if not ok:
            failed += 1
    sys.stdout.write("".join(chunks))
    print(f"files: {len(argv)}")
    if failed:
        print(f"result: fail {failed}")
        return 1
    print("result: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
