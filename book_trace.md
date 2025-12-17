# Book Traceability Report (教材溯源表)

**Course:** Financial Mathematics: Theory and AI Application (Fall 2025)  
**Student:** Ma Weixiang (马伟祥) | 25214020012  
**Textbook:** Dixon, M. F., Halperin, I., & Bilokon, P. (2020). *Machine Learning in Finance: From Theory to Practice*. Springer.

---

## 溯源清单 / Traceability Matrix

| ID | 关键概念 / 算法 (Concept/Algorithm) | 教材章节 (Chapter & Section) | 对应 Notebook (Code Source) | 应用描述 (How it was applied in the Report) |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **High-Frequency Market Making (MDP)** | **Ch. 9, Section 9.4** <br> (Case Study 2: Market Making) | `ML_in_Finance_MarketMaking.ipynb` | 在 Q1 中，我使用了教材定义的 MDP 五元组 $(S, A, P, R, \gamma)$，特别是采用了教材中的库存惩罚奖励函数 $r_t = \Delta W_t - \eta q_t^2$ 来控制做市商的存货风险。 |
| **2** | **Fitted Q-Iteration (FQI)** | **Ch. 9, Section 9.6** <br> (Batch Reinforcement Learning) | `ML_in_Finance_FCW.ipynb` (Adapted logic) | 在 Q1 中，针对离线 LOB 数据，我使用了 FQI 算法，将 Bellman 更新转化为监督回归问题（如 XGBoost），解决了在线探索成本过高的问题。 |
| **3** | **QLBS Model (Q-Learner in Black-Scholes)** | **Ch. 10, Section 10.3** <br> (The QLBS Model) | `ML_in_Finance_QLBS_Option_Pricing.ipynb` | 在 Q2 中，我复现了 QLBS 模型架构，使用了最小化对冲方差和交易成本的奖励函数：$-(\Delta \hat{C} - a \Delta S)^2 - \lambda | \Delta a |$。 |
| **4** | **Analytic Optimal Action (Quadratic Q)** | **Ch. 10, Eq. 10.25** <br> (Analytic Solution) | `ML_in_Finance_QLBS_Option_Pricing.ipynb` | 在 Q2 算法实现中，利用 Q 函数关于动作 $a_t$ 的二次结构，直接实现了最优动作的解析解公式 $a^* = - \mathbf{u}\Phi / (2\mathbf{v}\Phi)$，避免了数值优化。 |
| **5** | **MaxEnt IRL (Maximum Entropy Inverse RL)** | **Ch. 11, Section 11.3** <br> (MaxEnt IRL) | `ML_in_Finance_IRL_FCW.ipynb` | 在 Q3 中，我使用了最大熵原理来恢复专家的奖励函数，通过“特征期望匹配” ($\mathbb{E}_{\pi_E}[\phi] = \mathbb{E}_{\pi}[\phi]$) 来解决行为克隆的鲁棒性问题。 |
| **6** | **Information Bottleneck (IB)** | **Ch. 12 (Frontiers)** <br> (Information Theoretic Tools) | N/A (Theoretical Extension) | 在 Q4 原型设计中，我结合了教材第12章关于信息论工具的讨论，引入信息瓶颈正则项 $\min I(O; Z) - \beta I(Z; R)$ 来提升 LLM 在噪声 Prompt 下的决策鲁棒性。 |

---

## 补充说明 / Notes

1. **代码复现性**：Q1 和 Q3 的实验代码逻辑深度参考了教材提供的官方 GitHub 仓库 (`mfrdixon/ML_Finance_Codes`) 中的实现逻辑，并针对本次考试的参数进行了调整。
2. **理论扩展**：Q4 的设计虽然基于教材 Ch.12 的理论基础，但结合了现代 LLM (Large Language Model) 的架构（POMDP Encoder），属于基于教材理论的创新应用。