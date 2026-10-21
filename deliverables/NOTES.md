# Notes (lite)

## English

This subset is one Declarative Jenkinsfile: `Jenkinsfile.simple`. It uses `agent any`, parameters (`PACK_ENV`, `PACK_DEPLOY_HOST`, `PACK_RUN_PACKAGE`), checkout, test, and an optional package stage. The sample host is `app.example.com`.

`check_jenkinsfile.py` checks brace balance and required directive words. It does not start Jenkins.

`python:3.12` is not the image in this file. The docker-agent file and the matrix stub are in the full pack. Check upstream docs before you add an image, a label, or a plugin option.

`checkout scm` uses the job SCM configuration. Check upstream docs.

## 中文

这个子集只有一份声明式 Jenkinsfile：`Jenkinsfile.simple`。它使用 `agent any`、参数（`PACK_ENV`、`PACK_DEPLOY_HOST`、`PACK_RUN_PACKAGE`）、检出、测试，以及一个可选的打包阶段。示例主机是 `app.example.com`。

`check_jenkinsfile.py` 检查花括号和必要指令。它不启动 Jenkins。

这份文件里没有 `python:3.12`。docker agent 和矩阵草稿在完整版里。添加镜像、label 或插件选项之前请 check upstream docs。

`checkout scm` 使用任务上的 SCM 配置。请 check upstream docs。
