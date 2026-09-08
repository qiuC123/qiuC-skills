# qiuC Skills

`qiuC-skills` 是供 Agent 安装的能力说明仓库。它保存调用流程、安全边界和工具依赖，
不保存大型可执行文件，也不替代实际工具的源码仓库。

## 仓库关系

| Skill | 实际工具来源 | 关系 |
|---|---|---|
| [`wechat-oa`](wechat-oa) | [`qiuC-tools/CLI/wechat-oa`](https://github.com/qiuC123/qiuC-tools/tree/main/CLI/wechat-oa) | Skill 从 `qiuC-tools` 的固定 Release 下载并校验 Windows 工具 |
| [`agent-reach`](agent-reach) | [`Panniantong/Agent-Reach`](https://github.com/Panniantong/Agent-Reach) | 上游 Skill 的审阅副本，并增加微信公众号适配 |
| [`story-wechat-writer`](story-wechat-writer) | 公众号故事写作规则 | 将电影、动画与漫画讲给没看过作品的读者听；只负责正文与必要资料说明 |
| [`story-wechat-producer`](story-wechat-producer) | 本地影片/字幕或漫画页图、可用媒体与文档工具；附 Python 初始化脚本 | 核对来源、回改文案、提取截图/图格、排版并检查公众号图文与 DOCX |
| [`story-video-writer`](story-video-writer) | 视频文案与素材编排参考 | 影视设计旁白与原片原声交替，漫画设计旁白与页格展示；交付干净配音稿及编排表 |
| [`story-video-producer`](story-video-producer) | 当前环境可用的写作、媒体、剪辑与 HyperFrames 能力 | 衔接来源核查、回改、配音、试排和实际成片检查；也可接续已有普通视频局部任务 |

`wechat-oa` 按固定 Release 使用 `qiuC-tools` 的工具，`agent-reach` 按需使用其上游平台后端。

安装 Skill 不等于已经安装实际 CLI。Skill 应先检查命令是否存在，再按照各自文档指向的
官方源码或固定 Release 安装工具；下载、持久安装和 `PATH` 修改仍需用户明确授权。

## 四个故事解说 Skill

按交付媒介与职责选入口，电影、动画电影、动画剧集、漫画/条漫在各入口内区分素材来源。
`story` 是这组工作流的命名，不表示已为小说、有声书等其他材料提供专门制作分支。

| 本次目标 | 使用方式 |
| --- | --- |
| 只写公众号正文 | `story-wechat-writer` |
| 核对来源、配图、制作公众号图文或 DOCX | `story-wechat-producer`，写稿环节使用 `story-wechat-writer` |
| 只写视频旁白与素材安排 | `story-video-writer` |
| 核素材、回改、配音、剪辑或完整视频 | `story-video-producer`，写稿环节使用 `story-video-writer` |

写作与制作技能的目录、`references/` 和所需 `scripts/` 均需完整保留；文件存在不等于客户端已发现或安装。
只有字幕/OCR 时可先交有依据的草稿和素材候选，有原片/漫画原页时核查后再调整文字及视觉安排。
可以在同一环境完成，也可以携带稿件、素材记录和可访问路径交给本地 Codex 继续，不要求固定应用分工。
公众号正文与视频旁白共享事实，但分别组织叙事；制作指令、来源定位和未核事项放在正文外。

| 原作素材 | 来源定位与制作差异 |
| --- | --- |
| 电影、动画电影 | 版本与源文件，字幕候选时间和已验证视频切点分别记录 |
| 动画剧集 | 季/集/篇章边界，每集独立源文件和源时间；不把多集时间直接拼成最终时间线 |
| 漫画、条漫 | 卷章、文件页与印刷页、格序/纵向区域及阅读方向；实看原页核对 OCR、气泡归属与裁切 |

影视视频默认保留横向原片并安排旁白与原声，兼顾抖音竖屏浏览和全屏观看；漫画按页格和文字可读性确定展示。
漫画新增的角色配音属于演绎，不能称为原作原声。用户指定的画幅、范围与交付阶段优先。

## 名称迁移

| 旧名称 | 新名称 |
| --- | --- |
| `anime-film-commentary-writer`（此前为个人写作 skill） | `story-wechat-writer`，收敛为公众号写作，并加入本仓库 |
| `movie-wechat-illustrated-explainer` | `story-wechat-producer` |
| `anime-film-video-writer` | `story-video-writer` |
| `self-media-video-router` | `story-video-producer` |

更新文件夹名、`SKILL.md` 的 `name`、UI 默认提示词及调用关系。安装时同步已确认属于这四个 skill 的旧副本，保留用户自定义修改；不要同时留下新旧两套自动触发入口。
本仓库不保留重复别名 skill。已有公众号项目继续读取原工程，单片初始化的 `--video`/`--subtitle` 参数仍兼容；不要为了改名重建已有工程或重置素材记录。

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
