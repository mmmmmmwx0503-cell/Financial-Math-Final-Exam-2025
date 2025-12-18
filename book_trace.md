# 教材溯源记录表 (Book Traceability Report)

**课程名称:** Financial Mathematics: Theory and AI Application (Fall 2025)  
**学生姓名:** 马伟祥 (25214020012)  
**参考教材:** Dixon, M. F., Halperin, I., & Bilokon, P. (2020). *Machine Learning in Finance: From Theory to Practice*. Springer.

---

## 溯源清单 (Traceability Matrix)

| ID | 关键概念 / 算法 | 教材章节 (Chapter & Section) | 对应 Notebook (Code Source) | 实践应用与扩展说明 (Modifications & Extensions) |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **MDP Modeling for Market Making** | **Ch. 9, Section 9.4** <br> (Case Study 2: Market Making) | `ML_in_Finance_MarketMaking.ipynb` | **原始概念**：教材定义了做市商的基本 MDP 五元组。<br>**我的扩展**：在奖励函数中显式引入了 Avellaneda-Stoikov 风格的**库存惩罚项** ($-\eta q_t^2$)，迫使策略在库存偏离时进行均值回归，增强了风险控制能力。 |
| **2** | **Poisson Process for LOB Dynamics** | **Ch. 9, Section 9.4.1** <br> (Limit Order Book Dynamics) | `ML_in_Finance_MarketMaking.ipynb` | **原始概念**：假设限价单到达服从泊松过程，强度 $\lambda(\delta) = A e^{-k\delta}$。<br>**我的应用**：在模拟环境构建中，使用了该理论模型来生成订单流，并校准了 $A$ 和 $k$ 参数以模拟高波动率市场环境。 |
| **3** | **Fitted Q-Iteration (FQI)** | **Ch. 9, Section 9.6** <br> (Batch Reinforcement Learning) | `ML_in_Finance_FCW.ipynb` (Adapted logic) | **原始概念**：将 RL 问题转化为监督回归以处理离线数据。<br>**我的修改**：针对金融时间序列的非平稳性，在回归器选择上使用了 XGBoost 并强调了特征工程（如时间剩余 $T-t$），并在评估环节引入了 OPE (Fitted Q Evaluation)。 |
| **4** | **QLBS Model (Q-Learner in Black-Scholes)** | **Ch. 10, Section 10.3** <br> (The QLBS Model) | `ML_in_Finance_QLBS_Option_Pricing.ipynb` | **原始概念**：利用 BS 模型推导 Q-learning 框架。<br>**我的扩展**：在模拟环境中加入了**成比例交易成本** ($\lambda |a_t - a_{t-1}|$)，使得实验环境不再是理想的无摩擦市场，从而验证了 QLBS 相比 BS Delta 对冲在减少换手率方面的优势。 |
| **5** | **Analytic Optimal Action (Closed-form)** | **Ch. 10, Eq. 10.25** <br> (Analytic Solution) | `ML_in_Finance_QLBS_Option_Pricing.ipynb` | **原始概念**：利用 Q 函数的二次结构直接求导得到最优动作。<br>**我的应用**：在代码实现中，我放弃了数值优化方法（如 SGD），严格实现了该解析解公式，并加入了动作截断 (Clipping) 逻辑以防止在深度虚值区域因 $\mathcal{A}_t \to 0$ 导致的数值爆炸。 |
| **6** | **Basis Functions (Laguerre Polynomials)** | **Ch. 10, Section 10.3.3** <br> (Implementation Details) | `ML_in_Finance_QLBS_Option_Pricing.ipynb` | **原始概念**：使用 Laguerre 多项式作为基函数 $\Phi(S)$ 来逼近 Q 值。<br>**我的应用**：在回归步骤中，选择了前 3 阶 Laguerre 多项式以平衡偏差与方差，并应用了 Tikhonov 正则化 (Ridge) 来处理基函数矩阵的病态问题。 |
| **7** | **MaxEnt IRL (Maximum Entropy Inverse RL)** | **Ch. 11, Section 11.3** <br> (MaxEnt IRL) | `ML_in_Finance_IRL_FCW.ipynb` | **原始概念**：通过最大化熵来解决奖励函数的不确定性问题。<br>**我的修改**：针对催收场景，在特征工程中去除了 UserID 等 ID 类特征，改用**泛化特征**（如 Risk Score, DTI），以解决教材中提到的“奖励函数过拟合”问题。 |
| **8** | **Feature Expectation Matching** | **Ch. 11, Eq. 11.12** <br> (Feature Matching) | `ML_in_Finance_IRL_FCW.ipynb` | **原始概念**：IRL 的目标是寻找一个策略，使其特征期望等于专家的特征期望。<br>**我的应用**：在代码的训练循环中，显式计算了 `expert_feature_expectations - learner_feature_expectations` 作为梯度更新奖励权重，验证了该理论的有效性。 |
| **9** | **POMDP Architecture** | **Ch. 12, Section 12.2** <br> (Partially Observable MDPs) | N/A (Architecture Design) | **原始概念**：在部分可观测环境下，智能体无法直接获取真实状态 $s_t$。<br>**我的应用**：在 Q4 系统设计中，利用 LLM 作为状态编码器 $z_t = f_\phi(o_t)$，将非结构化文本观测转化为隐状态表征，构建了标准的 POMDP 决策流。 |
| **10** | **Information Bottleneck (IB)** | **Ch. 12 (Frontiers)** <br> (Information Theoretic Tools) | N/A (Theoretical Extension) | **原始概念**：教材 Ch.12 讨论了信息论工具在 RL 中的应用。<br>**我的扩展**：我将 IB 理论具体化为 $\min I(O;Z) - \beta I(Z;R)$ 的正则化项，设计了具体的实验来验证其在 Prompt 噪声攻击下的鲁棒性，体现了对前沿理论的迁移应用。 |

---

## 补充说明

1. **代码复现性**：Q1, Q2, Q3 的核心算法逻辑均基于教材官方 GitHub 仓库 (`mfrdixon/ML_Finance_Codes`) 中的实现逻辑进行了适配。
2. **理论深度**：Q4 的设计虽然没有直接对应的 Notebook，但其理论基础严格遵循教材第 12 章关于“感知-行动循环”和“信息正则化”的讨论。