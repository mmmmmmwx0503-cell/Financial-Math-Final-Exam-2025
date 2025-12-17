# LLM 深度协作与审计日志 (LLM Deep Collaboration & Audit Log)

**课程名称:** Financial Mathematics: Theory and AI Application (Fall 2025)  
**学生姓名:** 马伟祥 (25214020012)  
**提交日期:** 2025年12月17日  

---

## 1. 执行摘要 (Executive Summary)

本日志详细记录了在完成期末大作业过程中，学生（Human）与 AI 助手（Gemini 3 Pro）的深度协作全过程。

**核心原则：** AI 仅被视为“初级程序员”和“文档助理”。所有涉及**模型选型**、**数学原理推导**、**超参数设定**以及**系统架构设计**的关键决策，均由学生依据教材 *Machine Learning in Finance (Dixon et al., 2020)* 及配套 Notebooks 进行严格的人工核验、辩论与修正。

**交互统计：**
* **总交互轮数：** 12 轮
* **有效采纳率：** 约 25% (主要集中在 LaTeX 排版与基础绘图代码)
* **人工修正/驳回率：** 约 75% (涉及核心算法逻辑、理论对齐、工程落地)

---

## 2. 详细交互审计 (Detailed Interaction Audit)

本部分按题目顺序，详细记录了每一道题目的“AI 提案 -> 人工审计 -> 最终决策”过程。

### 🛑 阶段一：环境与教材对齐 (Setup & Alignment)
| 交互节点 | AI 初始输出 / 建议 | 人工审计与干预 (Human Intervention) | 决策依据 (Source of Truth) |
| :--- | :--- | :--- | :--- |
| **教材识别** | AI 扫描文件列表后，错误地将 *Martingale Methods* (Musiela & Rutkowski) 识别为核心理论依据，试图使用鞅论解题。 | **【严重驳回】**<br>立即终止该思路。明确指出考试要求基于 *Dixon et al. (2020)* 的机器学习方法，而非传统的随机分析。要求 AI 锁定 Ch.9-12 范围。 | **Exam_Question.pdf**<br>(Exam Goals: Book Traceability) |
| **考点拆解** | AI 建议 Q4 可以自由发挥，讨论 Fintech 宏观趋势。 | **【修正】**<br>指出 Q4 必须结合 Ch.12 的具体技术点（信息论、漂移监控），不能泛泛而谈，要求具体落实到“感知-决策闭环”架构。 | **Dixon Ch.12**<br>(Frontiers) |

---

### 🛑 阶段二：Q1 做市商策略 (Market Making)
| 交互节点 | AI 初始输出 / 建议 | 人工审计与干预 (Human Intervention) | 决策依据 (Source of Truth) |
| :--- | :--- | :--- | :--- |
| **动作空间定义** | AI 建议使用连续动作空间 $a_t \in \mathbb{R}^2$ (Continuous Spread)，并建议使用 PPO 算法。 | **【工程修正】**<br>检查 `ML_in_Finance_MarketMaking.ipynb` 后，发现代码实现是基于**离散动作** (Tight/Neutral/Wide)。为了确保实验可复现，我强制要求将定义修改为离散空间，并改用 Value-based 方法。 | **Reference Code**<br>(Line 82: Discrete Actions) |
| **算法选型** | 针对离线 LOB 数据，AI 建议使用 DQN (Deep Q-Network)。 | **【理论驳回】**<br>DQN 在离线数据上存在严重的高估偏差 (Overestimation Bias)。根据教材 Sec 9.6，针对 Batch RL 场景，**Fitted Q-Iteration (FQI)** 是更稳健的选择。 | **Dixon Ch.9 Sec 9.6**<br>(Batch RL) |
| **奖励函数迭代** | AI 最初仅设定最大化 PnL：$r_t = \Delta W_t$。 | **【深度修正】**<br>做市商的核心风险是库存积压。我要求必须加入库存惩罚项 $-\eta q_t^2$，并微调 $\eta$ 系数以实现均值回归效果。 | **Avellaneda-Stoikov (2008)**<br>教材案例 9.6 |

---

### 🛑 阶段三：Q2 期权对冲 (QLBS)
| 交互节点 | AI 初始输出 / 建议 | 人工审计与干预 (Human Intervention) | 决策依据 (Source of Truth) |
| :--- | :--- | :--- | :--- |
| **求解方法** | AI 建议使用标准的 SGD 梯度下降来更新 Q 网络。 | **【理论驳回】**<br>这是本题的关键得分点。教材 Ch.10 (Sec 10.3) 明确推导了 QLBS 的**解析解 (Closed-form Solution)**。我要求 AI 推导并使用 Eq 10.25 公式，而非数值近似。 | **Dixon Ch.10 Eq 10.25**<br>(Analytic Q-Learning) |
| **基函数选择** | AI 建议使用复杂的神经网络作为函数逼近器。 | **【修正】**<br>为了配合解析解，Q 函数必须是基函数的线性组合。我指定使用 **Laguerre 多项式** 或简单的幂基函数 $\Phi(S) = [1, S, S^2]$，这与 Notebook 实现一致。 | **ML_in_Finance_QLBS.ipynb** |
| **摩擦建模** | AI 忽略了交易成本，假设无摩擦市场。 | **【修正】**<br>强调实验必须包含交易成本 $\lambda |a_t - a_{t-1}|$，否则 QLBS 相比 BS Delta 对冲就没有优势了。 | **Exam Goal**<br>(Real-world constraints) |

---

### 🛑 阶段四：Q3 逆强化学习 (IRL)
| 交互节点 | AI 初始输出 / 建议 | 人工审计与干预 (Human Intervention) | 决策依据 (Source of Truth) |
| :--- | :--- | :--- | :--- |
| **算法辨析** | AI 混淆了“行为克隆 (BC)”和“逆强化学习 (IRL)”，建议直接模仿专家动作。 | **【概念纠偏】**<br>明确指出 BC 存在复合误差 (Compound Error) 且缺乏迁移性。必须使用 **MaxEnt IRL** 恢复奖励函数 $R(s)$，解释清楚“特征期望匹配”原理。 | **Dixon Ch.11 Sec 11.3** |
| **特征工程** | AI 建议使用原始的 State ID (如 UserID) 作为特征。 | **【工程修正】**<br>UserID 不具备泛化能力。我要求构建**可解释特征向量** (如：Risk Score, DTI Ratio, Promise Rate)，确保学到的 Reward 在新用户上依然有效。 | **System Robustness** |

---

### 🛑 阶段五：Q4 LLM 系统与代码工程
| 交互节点 | AI 初始输出 / 建议 | 人工审计与干预 (Human Intervention) | 决策依据 (Source of Truth) |
| :--- | :--- | :--- | :--- |
| **理论植入** | AI 提供的系统设计缺乏理论深度，仅是工程堆砌。 | **【理论提升】**<br>为了扣题 Ch.12，我要求引入 **Information Bottleneck (IB)** 正则化理论 ($\min I(O;Z) - \beta I(Z;R)$)，以此从信息论角度解释系统的抗噪性。 | **Dixon Ch.12**<br>(Information Theory) |
| **故障安全** | AI 建议：“如果 LLM 解析失败，就让用户重试”。 | **【驳回】**<br>金融系统不能依赖用户重试。我设计了确定性的 **规则回退 (Rule-Based Fallback)** 策略（如正则匹配、人工坐席接管）。 | **Operational Risk** |
| **代码报错修复** | AI 生成的绘图代码使用了 `seaborn.histplot`，导致 `pandas` 版本不兼容报错。 | **【工程阻断】**<br>拒绝了 AI 提出的“降级 pandas 版本”的建议。我重写了绘图逻辑，**移除 seaborn**，仅使用标准库 `matplotlib`，确保代码在任何 Python 环境下均可“一键复现”。 | **Python Best Practices** |

---

## 3. 幻觉监测报告 (Hallucination Audit Report)

在协作过程中，我监测到并拦截了以下 AI 幻觉（Hallucinations）：

1.  **虚构的代码库引用**：
    * *幻觉内容：* AI 曾试图调用 `mlfinlab` 库中的 `financial_data_structures` 模块。
    * *人工处理：* 考试环境未提供该第三方库。我强制要求仅使用 `numpy` 和 `scipy` 手写实现所有逻辑。

2.  **不存在的教材章节**：
    * *幻觉内容：* AI 曾提到“Ch.13 介绍了 LSTM 在高频交易中的应用”。
    * *人工处理：* 纠正 AI，Dixon 教材正文仅到 Ch.12。忽略该建议，严格限定范围在 Ch.9-12。

3.  **过度自信的错误建议**：
    * *幻觉内容：* AI 声称“QLBS 在任何情况下都优于 BS 模型”。
    * *人工处理：* 这是错误的。在无摩擦、符合几何布朗运动的理想市场中，BS 是最优的。QLBS 的优势仅在于**存在交易成本和离散对冲**的场景。我在报告中修正了这一结论。

---

## 4. 结论 (Conclusion)

本次作业的完成过程证明了：**AI 是高效的“副驾驶”和“代码打字员”，但绝不是“领航员”。**

通过对 AI 输出的每一行代码、每一个公式进行严格的 **Book Traceability (教材溯源)** 和 **逻辑审计**，我确保了最终提交的报告不仅符合复旦大学的学术规范，而且在工程上是可运行、可复现且鲁棒的。