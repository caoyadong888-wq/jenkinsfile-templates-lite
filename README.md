# Jenkinsfile Templates (lite)

## English

### Purpose

A free slice: one Declarative Jenkinsfile (`agent any`, parameters, checkout, test, optional package) and a local checker for braces and directives. The checker does not start Jenkins.

The full pack adds a docker-agent Jenkinsfile, a matrix stub, Chinese notes, and a filled shop pipeline with pytest.

### Deliverables

- `CHANGELOG.md` — version note for this lite subset.
- `deliverables/Jenkinsfile.simple` — the simple pipeline. Host `app.example.com`.
- `deliverables/NOTES.md` — short English and Chinese notes.
- `deliverables/check_jenkinsfile.py` — local structure checker.
- `examples/shop-api/src/app.py` — quote_total and health.
- `examples/shop-api/README.md` — how to call the helper without Jenkins.

### Quick start

```bash
python3 deliverables/check_jenkinsfile.py deliverables/Jenkinsfile.simple
```

Copy `Jenkinsfile.simple` to a repository root as `Jenkinsfile` when you want Jenkins to load it. Check upstream docs for the pipeline linter on your controller.

### Requirements

Python 3.9 or newer. Jenkins is not required to run the checker. A controller that accepts this Declarative file is required only when you actually run it. Check upstream docs.

## 中文

### 用途

免费子集：一份声明式 Jenkinsfile（`agent any`、参数、检出、测试、可选打包）以及一个检查花括号和指令的本地脚本。检查器不启动 Jenkins。

完整版另有 docker agent Jenkinsfile、矩阵草稿、中文长说明，以及一份带 pytest 的 shop 流水线。

### 交付清单

- `CHANGELOG.md` — 本精简子集的版本说明。
- `deliverables/Jenkinsfile.simple` — 简单流水线。主机 `app.example.com`。
- `deliverables/NOTES.md` — 简短的中英文说明。
- `deliverables/check_jenkinsfile.py` — 本地结构检查器。
- `examples/shop-api/src/app.py` — quote_total 和 health。
- `examples/shop-api/README.md` — 不启动 Jenkins 时如何调用这个模块。

### 快速开始

```bash
python3 deliverables/check_jenkinsfile.py deliverables/Jenkinsfile.simple
```

要让 Jenkins 加载时，把 `Jenkinsfile.simple` 复制到仓库根目录并命名为 `Jenkinsfile`。控制器上的流水线检查页请 check upstream docs。

### 环境要求

Python 3.9 或更高。只跑检查器时不需要 Jenkins。真正运行这份流水线时，控制器需要接受这些声明式指令。请 check upstream docs。

Full version: GUMROAD_URL
