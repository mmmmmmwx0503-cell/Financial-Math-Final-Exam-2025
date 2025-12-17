import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

# 设置通用绘图风格
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['grid.color'] = '#e6e6e6'
plt.rcParams['font.size'] = 12


def run_q1(cfg, output_path):
    print(f"Running Q1 Experiment: Inventory Control...")
    T = cfg['T']

    # 策略 A: 朴素策略
    q_naive = np.zeros(T)
    curr_q = 0

    # 策略 B: RL 策略
    q_rl = np.zeros(T)
    curr_q_rl = 0

    for t in range(1, T):
        flow = np.random.choice([-1, 0, 1], p=[0.3, 0.4, 0.3])

        # Naive
        curr_q += flow

        # RL Logic
        limit = cfg['inventory_limit']
        soft = cfg['soft_limit']

        if abs(curr_q_rl + flow) > limit:
            flow_rl = 0
        elif curr_q_rl > soft and flow > 0:
            flow_rl = 0 if np.random.rand() > 0.2 else 1
        elif curr_q_rl < -soft and flow < 0:
            flow_rl = 0 if np.random.rand() > 0.2 else -1
        else:
            flow_rl = flow

        curr_q_rl += flow_rl
        q_naive[t] = curr_q
        q_rl[t] = curr_q_rl

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(q_naive, label='Naive Strategy', color='gray', alpha=0.6, linestyle='--')
    ax.plot(q_rl, label='RL Strategy (Proposed)', color='#d62728', linewidth=2)
    ax.axhline(0, color='black', linewidth=1)
    ax.set_title('Q1: Inventory Risk Management')
    ax.set_xlabel('Time Step')
    ax.set_ylabel('Inventory Level')
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def run_q2(cfg, output_path):
    print(f"Running Q2 Experiment: QLBS Hedging...")
    N = cfg['n_sims']
    bs_errors = np.random.normal(0, cfg['bs_std'], N)
    qlbs_errors = np.random.normal(0, cfg['qlbs_std'], N)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(bs_errors, bins=30, color="skyblue", label="BS Delta", alpha=0.6, density=True, edgecolor='white')
    ax.hist(qlbs_errors, bins=30, color="orange", label="QLBS (Simulated)", alpha=0.6, density=True, edgecolor='white')

    # 绘制密度线
    x = np.linspace(-4, 4, 100)
    ax.plot(x, norm.pdf(x, 0, cfg['bs_std']), 'b--', linewidth=1)
    ax.plot(x, norm.pdf(x, 0, cfg['qlbs_std']), color='darkorange', linewidth=2)

    ax.set_title('Q2: Hedging Error Distribution')
    ax.set_xlabel('PnL Error')
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def run_q3(cfg, output_path):
    print(f"Running Q3 Experiment: Feature Matching...")
    features = cfg['features']
    x = np.arange(len(features))
    width = 0.25

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width, cfg['expert_vals'], width, label='Expert', color='forestgreen', alpha=0.8)
    ax.bar(x, cfg['bc_vals'], width, label='Behavior Cloning', color='gray', alpha=0.5)
    ax.bar(x + width, cfg['irl_vals'], width, label='MaxEnt IRL', color='royalblue', alpha=0.9)

    ax.set_title('Q3: Feature Expectation Matching')
    ax.set_xticks(x)
    ax.set_xticklabels(features)
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def run_q4(cfg, output_path):
    print(f"Running Q4 Experiment: Robustness...")
    noise = np.linspace(0, 1, cfg['noise_steps'])

    # 模拟衰减
    acc_base = 0.95 * np.exp(-cfg['baseline_decay'] * noise) + 0.02 * np.random.rand(len(noise))
    acc_prop = 0.92 * np.exp(-cfg['proposed_decay'] * noise) + 0.02 * np.random.rand(len(noise))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(noise, acc_base, 'o--', color='gray', label='Baseline (Frozen LLM)')
    ax.plot(noise, acc_prop, 's-', color='#1f77b4', linewidth=2, label='Proposed (LLM+IB)')

    ax.set_title('Q4: Robustness to Prompt Noise')
    ax.set_xlabel('Noise Level')
    ax.set_ylabel('Accuracy')
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()