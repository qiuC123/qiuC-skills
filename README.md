# qiuC Skills

`qiuC-skills` 是供 Agent 安装的能力说明仓库。它保存调用流程、安全边界和工具依赖，
不保存大型可执行文件，也不替代实际工具的源码仓库。

## 仓库关系

| Skill | 实际工具来源 | 关系 |
|---|---|---|
| [`wechat-oa`](wechat-oa) | [`qiuC-tools/CLI/wechat-oa`](https://github.com/qiuC123/qiuC-tools/tree/main/CLI/wechat-oa) | Skill 从 `qiuC-tools` 的固定 Release 下载并校验 Windows 工具 |
| [`wxcli`](wxcli) | 同一个 WeChat OA 工具 | 仅保留旧名称兼容，新接入优先使用 `wechat-oa` |
| [`agent-reach`](agent-reach) | [`Panniantong/Agent-Reach`](https://github.com/Panniantong/Agent-Reach) | 上游 Skill 的审阅副本，并增加微信公众号适配 |

关系可以概括为：

```text
Agent 安装 qiuC-skills
        │
        ├─ wechat-oa Skill ──下载固定 Release──> qiuC-tools/CLI/wechat-oa
        └─ agent-reach Skill ──安装或升级工具──> Panniantong/Agent-Reach
```

安装 Skill 不等于已经安装实际 CLI。Skill 应先检查命令是否存在，再按照各自文档指向的
官方源码或固定 Release 安装工具；下载、持久安装和 `PATH` 修改仍需用户明确授权。

## Agent Reach 同步策略

本仓库中的 `agent-reach` 是普通文件副本，不是 Git submodule，也不会自动跟随上游仓库。
`agent-reach check-update` 检查的是用户机器上安装的 Agent Reach 工具版本，不会修改本
仓库中的 Skill 文件。

上游更新后，维护者需要比较
`Panniantong/Agent-Reach/agent_reach/skill` 与本仓库的 `agent-reach`，审阅并同步适用的
变更，同时保留本仓库的微信公众号路由和 `references/wechat.md`。不要直接覆盖本地适配。

## 维护规则

- CLI 参数、JSON 契约或安全流程变化时，先更新并发布工具，再同步相关 Skill。
- WeChat OA 版本标签使用 `wechat-oa-v<版本>`，不同 CLI 的版本互不冲突。
- Skill 中的下载链接必须固定到明确版本和 SHA-256，不能默认使用不稳定的 `latest` 文件。
