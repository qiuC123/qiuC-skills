# qiuC Skills

`qiuC-skills` 是供 Agent 安装的能力说明仓库。它保存调用流程、安全边界和工具依赖，
不保存大型可执行文件，也不替代实际工具的源码仓库。

## 仓库关系

| Skill | 实际工具来源 | 关系 |
|---|---|---|
| [`wechat-oa`](wechat-oa) | [`qiuC-tools/CLI/wechat-oa`](https://github.com/qiuC123/qiuC-tools/tree/main/CLI/wechat-oa) | Skill 从 `qiuC-tools` 的固定 Release 下载并校验 Windows 工具 |
| [`agent-reach`](agent-reach) | [`Panniantong/Agent-Reach`](https://github.com/Panniantong/Agent-Reach) | 上游 Skill 的审阅副本，并增加微信公众号适配 |
| [`movie-wechat-illustrated-explainer`](movie-wechat-illustrated-explainer) | 本地电影、字幕与 FFmpeg；附 Python 项目初始化脚本 | 按阶段核对剧情、规划原片截图并制作公众号图文解说与 DOCX |
| [`anime-film-video-writer`](anime-film-video-writer) | 文案规则及原片插入表参考 | 面向没看过作品的观众，写作或改写旁白与原片共同叙事的视频文案；不执行媒体制作 |
| [`self-media-video-router`](self-media-video-router) | 当前环境可用的写作、媒体、剪辑与 HyperFrames 能力 | 衔接字幕、原片候选、核片、回改文案与制作；也保留其他自媒体视频任务入口 |

关系可以概括为：

```text
Agent 安装 qiuC-skills
        │
        ├─ wechat-oa Skill ──下载固定 Release──> qiuC-tools/CLI/wechat-oa
        └─ agent-reach Skill ──安装或升级工具──> Panniantong/Agent-Reach
```

安装 Skill 不等于已经安装实际 CLI。Skill 应先检查命令是否存在，再按照各自文档指向的
官方源码或固定 Release 安装工具；下载、持久安装和 `PATH` 修改仍需用户明确授权。

## 影视视频工作流

做“解说＋原片”视频时，配套使用 `self-media-video-router` 与 `anime-film-video-writer`。
两份 skill 的目录与 `references/` 均需完整保留；仓库中存在文件不代表当前客户端已安装。
只有字幕时先交故事草稿与原片候选，有原片时再核实画面、声音与切点，并据此回改文案。
可以在同一环境完成，也可以携带初稿、片段记录和素材位置交给本地 Codex 继续，不要求固定应用分工。
正文与制作记录分别交付；公众号图文使用独立流程，共用事实材料但不机械改写成视频。

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
