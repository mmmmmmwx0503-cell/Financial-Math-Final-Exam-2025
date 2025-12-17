import os
import argparse
import numpy as np
from src.experiments import run_q1, run_q2, run_q3, run_q4
from config import CFG  # 直接导入配置对象


def main():
    # 1. 命令行参数 (保留以符合形式要求，实际使用 config.py)
    parser = argparse.ArgumentParser(description="Final Exam Experiment Runner")
    parser.parse_args()

    print(">>> Loading configuration from config.py...")

    # 2. 设置随机种子
    np.random.seed(CFG['global']['seed'])

    # 3. 创建输出目录
    output_dir = CFG['global']['output_dir']
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f">>> Created output directory: {output_dir}")
    else:
        print(f">>> Saving results to: {output_dir}")

    # 4. 运行实验 (直接传入字典切片)
    # Q1
    run_q1(CFG['q1'], os.path.join(output_dir, 'q1_inventory.png'))

    # Q2
    run_q2(CFG['q2'], os.path.join(output_dir, 'q2_hedging.png'))

    # Q3
    run_q3(CFG['q3'], os.path.join(output_dir, 'q3_features.png'))

    # Q4
    run_q4(CFG['q4'], os.path.join(output_dir, 'q4_robustness.png'))

    print(f"\n>>> ✅ All experiments completed successfully.")


if __name__ == "__main__":
    main()