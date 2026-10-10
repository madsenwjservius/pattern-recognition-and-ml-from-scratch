# Pattern Recognition and Machine Learning From Scratch

Machine Learning Techniques implemented from scratch using Python, NumPy, Pandas and Matplolib, focusing on the theoretical foundations from *Pattern Recognition* (Duda, Hart & Stork) and *Introduction to Machine Learning* (Alpaydin, 4th ed.).

---

## Project Structure

```text
pattern-recognition-and-ml-from-scratch/
│
├── .gitignore              # Ignored build/cache files
├── environment.yml         # Conda environment specification
├── setup.py                # Local editable package configuration
├── README.md               # Project documentation and notes
│
├── data/                   # Local datasets and processing scripts
│   └── README.md           # Dataset sources and formats
│
├── src/                    # Source code (From-scratch algorithms in NumPy)
│   ├── __init__.py
│   ├── utils.py            # Dataset loading and general utilities
│   ├── bayes/              # Ch. 2 & 3: Bayesian Decision Theory & Classifiers
│   ├── estimation/         # Ch. 4: MLE, Bayesian Estimation, Nonparametric
│   ├── linear_models/      # Ch. 5 & 6: Linear Models & Dimensionality Reduction
│   └── clustering/         # Ch. 7: Unsupervised Learning (K-Means, GMM/EM)
│
├── math_foundations/       # Pure mathematical script derivations (Linear Algebra, etc.)
│
├── notebooks/              # Prototyping and visualization laboratory
│   ├── 00_tools/           # Mastery of NumPy, Pandas, Matplotlib & Sanity Checks
│   ├── 01_math/            # Translations of mathematical theorems into code
│   └── 02_experiments/     # Model experimentation using src/ classes
|
```

---

## Quickstart Installation Guide

Follow these steps to set up the repository locally on your machine:

```bash
# 1. Clone the repository and navigate inside
git clone github.com/madsenwjservius/pattern-recognition-and-ml-from-scratch
cd pattern-recognition-and-ml-from-scratch

# 2. Create the Conda environment from the configuration file
conda env create -f environment.yml

# 3. Activate the newly created environment
conda activate ml-scratch

# 4. Install the project locally in "editable" mode
pip install -e .

# 5. Launch Jupyter to start experimenting
jupyter notebook
```

---
