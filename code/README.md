# Financial Mathematics: Theory and AI Application - Final Exam Project

**Course:** Financial Mathematics: Theory and AI Application (Fall 2025)  
**Student:** Ma Weixiang (马伟祥)  
**Student ID:** 25214020012  
**Instructor:** Cao Lu  

---

## 📖 Project Overview

This repository contains the source code and reproduction scripts for the Final Exam Report. The project implements key algorithms from *Machine Learning in Finance* (Dixon et al., 2020) to address four specific financial problems:

1.  **Q1 (Chapter 9):** High-Frequency Market Making using Offline RL (Fitted Q-Iteration).
2.  **Q2 (Chapter 10):** Option Hedging using the QLBS model (Q-Learner in Black-Scholes).
3.  **Q3 (Chapter 11):** Inverse Reinforcement Learning (MaxEnt IRL) for Intelligent Collections.
4.  **Q4 (Chapter 12):** LLM-Augmented Decision Systems with Information Bottleneck regularization.

---

## 🚀 One-Click Reproduction (一键复现)

To reproduce all experiments and generate the plots used in the report, simply execute the following command in the root directory:

```bash
python main.py

---

##📂 Directory Structure
The project follows the strict structure required by the submission checklist:

Final_Exam_Code/
├── config.py               # [Config] Hyperparameters, seeds, and paths
├── main.py                 # [Entry Point] The one-click execution script
├── requirements.txt        # [Env] Dependencies (numpy, matplotlib, scipy)
├── README.md               # [Docs] This file
├── src/                    # [Source] Core algorithm implementations
│   ├── __init__.py
│   └── experiments.py      # Simulation logic for Q1-Q4
└── results/                # [Output] Auto-generated plots (Do not modify manually)
    ├── q1_inventory.png
    ├── q2_hedging.png
    ├── q3_features.png
    └── q4_robustness.png