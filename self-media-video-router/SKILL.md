---
name: self-media-video-router
description: Use when a user asks to plan, create, revise, render, or prepare a self-media or short-video project, including Douyin, Bilibili, scripts, storyboards, HyperFrames, footage, voiceover, captions, or release preparation, and the task needs the right installed Codex capability or professional agent selected.
---

# 自媒体视频创作路由

先按“任务阶段”路由，而不是一次加载全部能力。给出本次选用的能力、输入、产出和完成条件；只调用完成当前阶段所需的最少能力。

## 路由

| 任务或信号 | 首选能力 | 交付物 |
| --- | --- | --- |
| 选题、受众、钩子、口播脚本、分镜 | `prompt-engineer` | 创作简报、脚本、镜头表 |
| 新建、修改、检查、预览或渲染 HTML 视频 | `hyperframes` | 可编辑工程或 MP4；先读取项目 `AGENTS.md` |
| 素材、配音、BGM、音效、字幕、转录、背景处理 | `media-use` | 本地素材、素材台账或可粘贴配置 |
| 网址、热点、竞品、平台内容或资料调研 | `agent-reach` | 标明实际后端和证据层级的调研结论 |
| 事实、版权、夸大宣传、发布前风险 | `reality-checker` | 风险清单和可发布条件 |

若已安装对应专业 Agent，再补充路由：抖音策略 Agent 处理前三秒、完播率和发布文案；B 站策略 Agent 处理标题、封面、社区互动；内容创作或剪辑 Agent 处理脚本质量与剪辑节奏。未安装时，使用现有能力完成基础方案，并说明“可选安装”，不要把安装当作当前任务的一部分。

工程类 Agent 只在“制作或维护视频工具/代码项目”时使用；普通选题、脚本和发片不默认路由到它们。

## 执行顺序

1. 确认平台、目标、时长、素材来源和交付物；缺少且会影响方案时，只问一个最关键的问题。
2. 先产出创作简报，再产出脚本/分镜，然后制作、检查、发布准备。用户只要求某一阶段时，不擅自扩展到其他阶段。
3. 遇到 URL 或外部调研，必须使用 `agent-reach`；说明实际运行的后端。元数据、字幕/转录和真实音视频理解是不同证据层级，不能混为一谈。
4. 对 HyperFrames 项目，先使用 `hyperframes`，再由它选择 `hyperframes-core`、`hyperframes-animation`、`hyperframes-cli` 或其他子能力；修改 `.html` 后按项目约定运行完整检查。
5. 发布前交给 `reality-checker` 检查事实依据、素材授权、隐私、平台规则和“效果承诺”是否可证明。

## 安全边界

- Do not auto-install agents, plugins, CLIs, or platform backends. 需要新能力时，先说明用途、影响和安装选项，等待用户确认。
- Do not read Cookie, log in, upload, publish, spend money, or create external content without明确授权。
- Do not auto-update. 版本检查与实际更新分开；更新始终需要用户确认。
- 不把未验证的网页标题、平台元数据或 AI 推测写成已确认的事实。

## 收尾时的版本检查

完成一次较大的创作或多平台调研后，只检查本次实际用到且有官方检查命令的能力：

- 本次用 `agent-reach` 调研：收尾时运行 `agent-reach check-update`。
- 本次在某个 HyperFrames 工程工作：在该工程目录运行 `npx hyperframes@latest upgrade --project . --check`。

若发现新版，只在收尾报告一次，说明“有可选更新”和下一步命令；不要中断当前任务、不要自动升级、不要重复提醒同一版本。

## Example

用户说：“做一条 10 秒的抖音，讲 Codex 如何配合 HyperFrames 做视频。”

先由 `prompt-engineer` 给出钩子、口播与三段分镜；再通过 `hyperframes` 建立并检查竖屏视频；需要配音、字幕或 BGM 时转给 `media-use`；最后用 `reality-checker` 审查表述与素材。若用户要求研究抖音上的同类内容，再额外使用 `agent-reach`，而不是凭印象概括。
