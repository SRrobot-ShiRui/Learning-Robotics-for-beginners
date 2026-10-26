---
description: "2026 机器人大脑之战：Gemini Robotics 2、Figure Helix、Physical Intelligence π0 三条路线拆解，VLA 双系统架构、开源权重版图与数据瓶颈，全部信源标注，机器人炼金术前沿篇第 2 期"
---

> 本文是「前沿与译文」系列第 2 篇（主线 F2）。写作日期 2026-10-26，数据均标注来源与可信度评级，时效性内容请以最新信息为准。前置阅读：[第 02 篇 人形机器人 2026 现状](02-humanoid-2026-state.md)。

## 一、先讲一个选择困难症的故事

想象你是 2026 年的一家新人形机器人公司 CTO。本体你已经会造了——中国供应链能把整机价格压到一万美元级，躯干、腿部、关节模组都有现成货架方案。真正让你失眠的问题是：**给这台机器人装谁的"大脑"？**

装 Google 的？2026 年 7 月 30 日 DeepMind 发布 Gemini Robotics 2，公开演示里它能让人形机器人完成"看场景—理解指令—规划步骤—动手执行"的连贯操作，但只有早期合作伙伴能用（[Embodied Wire, 2026-09](https://embodiedwire.com/robot-foundation-models-compared)，可信度：高，逐条核对过模型版本与日期）。装 Figure 的？Helix 2.5 只跑在 Figure 自家机器人上，别人买不到。选 Physical Intelligence？π0 系列的权重在 GitHub 上随便下载，但它自己不造机器人。还是干脆自己练？英伟达把 GR00T N1.7 的 3B 权重开放商用，连参考硬件（Unitree G1）都给你配好了（同上）。

这个场景不是虚构——它是 2026 年所有本体厂商真实的必答题。也是本文想讲清楚的事：**身体正在变成商品，大脑才是战争**。

## 二、三条路线，三种赌注

### 路线 1：平台派——DeepMind 的"安卓时刻"

Gemini Robotics 2 的三个主打能力：全身协调控制（腿、躯干、手臂、手在一个神经回路里调度，而不是拼装多个单独训练的模块）、高级灵巧操作（会重新抓取、调整握姿）、多机器人协同（同一环境里多台机器人共享一个模型）（[Humanoid Robots UK, 2026-08](https://humanoidrobotsuk.com/insights/robot-ai-model-race)，可信度：中高，属分析文章，核心事实与 The Robot Report 报道一致）。

关键判断：DeepMind 不造机器人，它要做的是**模型主权**——配套与 Apptronik（Apollo 2）、Franka Duo 等本体的合作，复刻"安卓 + 手机厂商"的结构（同上）。对本体厂商这意味着低门槛，也意味着把命脉交给别人。

### 路线 2：垂直整合派——Figure 的"自产自销闭环"

Figure 的 Helix 把感知、推理、运动全塞进机载端到端系统。2026 年 1 月的 Helix 02 实现了从视觉输入到全身自主——一个神经网络从像素直出腿部、躯干、手臂、手指的指令，据称足以支撑 8 小时工厂班次无人工干预；5 月追加"人类示范迁移"（看人做一遍，机器人学会）；9 月 17 日迭代到 Helix 2.5（[Embodied Wire](https://embodiedwire.com/robot-foundation-models-compared)，可信度：高）。

架构上，Helix 是"双系统"的代表：System 2 是机载 VLM，以 7–9 Hz 做场景理解与任务规划；System 1 是反应式视觉运动策略，以 50–200 Hz 输出关节指令（[硅基参考, 2026](https://www.guijicankao.com/posts/vla-arch-humanoid-2026h1-shipment)，可信度：中高）。这个张力无法回避：70 亿参数级的推理太慢，关不上控制环；而高频控制又不需要每次都调用大模型。**把"想"和"动"分开，是人形机器人当前最务实的选择**——英伟达 GR00T、Google Gemini Robotics 都收敛到了同一范式。

Figure 的赌注是闭环：自研硬件 + 自研模型 + BMW 工厂的部署数据互喂。第 02 篇拆过那组数字——30 个陌生家庭 420 次尝试成功率 56%，去掉自家数据训练的对照模型只有 9%——同一套架构，只换数据，差 6 倍。工厂就是它的训练炉。

### 路线 3：纯模型派——Physical Intelligence 的"不造机器人"

π（pi）系列是软件优先论的最纯表达。π0 在 PaliGemma 骨干上外接一个 flow-matching"动作专家"，以约 50 Hz 生成连续动作块，兼顾灵巧操作需要的平滑与高频（[硅基参考](https://www.guijicankao.com/posts/vla-arch-humanoid-2026h1-shipment)，可信度：中高）；一个模型跨多个本体训练——在这台机器上叠衣服，在那台机器上装卸洗碗机。后续 π\*0.6 引入 advantage conditioning，把失败和人工纠错也变成训练信号，叠衣服、做咖啡任务成功率上到 90%（[DAMO 开发者矩阵](https://damodev.csdn.net/6aa6ef0a61de6467390ef87c.html)，可信度：中，技术博客综述）。

这家公司不造任何机器人，据多个来源报道正在以 110 亿美元以上估值融资约 10 亿美元（[Humanoid Robots UK](https://humanoidrobotsuk.com/insights/robot-ai-model-race)）。⚠️ 注意：另有来源称其估值为 24 亿美元（[Grandpa's AI](https://grandpasai.com/research/robotics/category/03-ai-autonomy.html)，可信度：低，与其余来源冲突，疑似未更新）。两个数字差 4 倍以上，**在交叉验证失败时，宁可存疑**——这正是读行业新闻的基本功。无论哪个数字为真，"不造一台机器人却拿到顶级估值"本身，就是市场对模型层价值的投票。

## 三、开源版图：谁把权重真的给了你

选大脑等于选供应商，开源与否决定了你是"用户"还是"囚徒"（[Embodied Wire, 2026-09-28](https://embodiedwire.com/robot-foundation-models-compared)，可信度：高）：

| 模型 | 开发方 | 最新版 | 权重开放 | 参数量 | 备注 |
|---|---|---|---|---|---|
| Isaac GR00T | NVIDIA | N1.7 | **完全开放商用** | 3B | 代码 Apache 2.0，GA |
| π 系列 | Physical Intelligence | π0.7 | 部分（π0/π0.5 开放） | 未披露 | openpi 仓库 Apache 2.0 |
| UnifoLM-WLA | 宇树 | 1.0 | 部分（4B 骨干开放） | ~6B | WLA-Base 未放出 |
| GO 系列 | 智元 | GO-2 | 仅旧版 GO-1 | 未披露 | CC BY-NC-SA 非商用 |
| Gemini Robotics | DeepMind | 2 | 否 | 未披露 | 早期合作伙伴 |
| Helix | Figure | 2.5 | 否 | 未披露 | 仅自家用 |
| GEN-1.5 / S1 | Generalist / Skild | — | 否 | 未披露 | 早期接入 |

值得单独一提的是参数规模的反向收缩：RT-2 做到 55B，OpenVLA 降到 7B，GR00T N1 只剩 2B——不是大模型不管用，是延迟卡在关节闭环上、端侧算力是硬约束，于是"双系统"长出来：慢的留大、快的做小（[DAMO 开发者矩阵](https://damodev.csdn.net/6aa6ef0a61de6467390ef87c.html)，可信度：中）。

## 四、绕不开的天花板：数据

语言语料以万亿 token 计，机器人数据却是遥操作一条条采的：体量最大的 Open X-Embodiment 汇聚 22 种本体、百万级轨迹，DROID 约 7.6 万条、350 小时，加总仍在**千小时量级**——比语言数据差六个数量级（[DAMO 开发者矩阵](https://damodev.csdn.net/6aa6ef0a61de6467390ef87c.html)，可信度：中高）。仿真可以补量，但要付 sim-to-real 的落差；真机采集可以保真，但硬件可靠性反过来卡数据产能——灵巧手"一周一换"的耐用性（下一篇文章的主题）直接决定了数据飞轮能转多快。

有来源称 2024 年以来机器人演示数据采集成本下降了约 60%（[Grandpa's AI](https://grandpasai.com/research/robotics/category/03-ai-autonomy.html)，可信度：低，单一来源，未见原始报告）。Physical Intelligence 的 EgoScale 论文则给出了第一个"机器人策略随数据量按可预测规律提升"的证据（同上，可信度：中）。如果 scaling law 在物理世界成立，这场战争的终局可能和 LLM 一样：赢家通吃，且赢家是数据最多的那个。

## 五、我怎么判断

给读者留三个可操作的判据：

1. **权重可下载 ≠ 可商用**。看清 license：GO-1 是非商用许可，拿它做产品等于埋雷。
2. **演示视频 ≠ 部署**。沿用第 02 篇的判据链：客户付费 > 免费试用 > 内部使用 > 演示视频。
3. **单一来源的数字先打折**。本文的估值矛盾就是现成的例子。

## 延伸阅读

- 本系列第 06 篇《灵巧手为什么这么难》：硬件可靠性如何卡住数据飞轮
- 本系列第 08 篇（预告）：《世界模型与 sim-to-real》：仿真里 100% 的机器人，到了仓库只有 30%
- 来源：[Embodied Wire 模型对比表](https://embodiedwire.com/robot-foundation-models-compared) · [Humanoid Robots UK 三强分析](https://humanoidrobotsuk.com/insights/robot-ai-model-race) · [硅基参考：VLA 架构与出货数据](https://www.guijicankao.com/posts/vla-arch-humanoid-2026h1-shipment) · [DAMO 开发者矩阵：VLA 技术综述](https://damodev.csdn.net/6aa6ef0a61de6467390ef87c.html)

**完整内容链接（三大模型逐维度对比、架构拆解与选型决策树）**：<https://blog.csdn.net/2301_81238088/category_13220213.html>

**完整版每周二更新**，订阅后第一时间推送。
