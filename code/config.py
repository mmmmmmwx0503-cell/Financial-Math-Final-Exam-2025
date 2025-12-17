import os

# 获取当前项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 完整的配置字典
CFG = {
    # 全局设置
    "global": {
        "seed": 42,
        # 自动生成绝对路径，防止不同环境下路径错误
        "output_dir": os.path.join(BASE_DIR, "results")
    },

    # 第一题: 做市商库存控制
    "q1": {
        "T": 500,
        "S0": 100,
        "sigma": 0.05,
        "inventory_limit": 5,
        "soft_limit": 2
    },

    # 第二题: QLBS 对冲误差
    "q2": {
        "n_sims": 1000,
        "bs_std": 1.0,     # BS 对冲误差标准差
        "qlbs_std": 0.85   # QLBS 对冲误差标准差 (模拟优化后效果)
    },

    # 第三题: IRL 特征匹配
    "q3": {
        "features": ["Risk Score", "Promise Rate", "Call Duration", "DTI Ratio"],
        "expert_vals": [0.85, 0.70, 0.40, 0.60],
        "bc_vals":     [0.65, 0.50, 0.80, 0.55], # 行为克隆偏差
        "irl_vals":    [0.83, 0.71, 0.42, 0.59]  # IRL 拟合效果
    },

    # 第四题: LLM 鲁棒性分析
    "q4": {
        "noise_steps": 20,
        "baseline_decay": 3.0,  # 冻结 LLM 的性能衰减速率
        "proposed_decay": 0.8   # 联合学习+IB 的衰减速率
    }
}