#  Finance Data Analysis & Risk Modeling

This repository contains a structured collection of quantitative finance projects focused on portfolio optimization, risk estimation, and systemic risk modeling. It is intended to demonstrate proficiency in financial theory, statistical modeling, and Python-based data analysis. The notebooks are modular and well-commented, making them suitable both for review and extension.

##  Project Objective

The goal of this repository is to showcase a variety of quantitative techniques used in modern finance, including:

- Portfolio theory and asset allocation (Markowitz, Black-Litterman)
- Value at Risk (VaR) estimation and backtesting
- Systemic risk measurement using CoVaR and ΔCoVaR
- Empirical data analysis and financial risk visualization

This portfolio highlights practical implementation skills that are directly applicable to roles in quantitative analysis, investment risk, and financial engineering.

---

##  Repository Structure

### `portfolio_optimization/`

Includes classical and advanced portfolio construction methods based on historical returns of US tech stocks:

- `1_markowitz.ipynb`: Builds Global Minimum Variance and Tangency portfolios using Modern Portfolio Theory, visualizes the efficient frontier and Capital Allocation Line.
- `2_black_litterman.ipynb`: Applies the Black-Litterman model to incorporate subjective investor views and compares results against the Markowitz tangency portfolio, including a neutral "zero-view" case.

**Key skills**: asset allocation, risk-return tradeoff, implied equilibrium returns, Bayesian portfolio theory.

---

### `value-at-risk/`

Implements risk management methods based on Value at Risk, aligned with Basel II capital requirements:

- `1_basic_descriptive_analysis.ipynb`: Time series analysis, return distributions, rolling statistics for individual assets.
- `2_VaR_Backtesting_Basel_II.ipynb`: Calculates 1-day and 10-day Historical Simulation VaR and backtests using Kupiec and Christoffersen tests.
- `3_montecarlo_var_backtesting_basel2_individual_portfolio.ipynb`: Simulates portfolio VaR via Monte Carlo methods and performs Basel II regulatory capital estimation.

**Key skills**: VaR, risk backtesting, statistical tests, Monte Carlo simulation, regulatory finance.

---

### `covar_delta_covar/`

Estimates **CoVaR** and **ΔCoVaR** based on quantile regression:

- `CoVaR_DeltaCoVaR_Analysis.ipynb`: Measures systemic risk contribution of a systemically important financial institution relative to a banking sector index.

**Key skills**: systemic risk, quantile regression, tail dependencies, financial stability analysis.

---

### `0_data/`

This folder contains cleaned datasets used across projects. Raw financial data are preprocessed here for modeling purposes.

---

##  Technologies & Tools

- Python (NumPy, pandas, matplotlib, seaborn, statsmodels, scikit-learn)
- Jupyter Notebooks
- Financial theory: Modern Portfolio Theory, CAPM, Black-Litterman, VaR
- Statistical methods: quantile regression, backtesting, hypothesis testing

---

##  Use Case

This repository was created as a showcase of applied quantitative finance for professional purposes. It is suitable for:

- Applications to roles in **Quantitative Research**, **Risk Analytics**, or **Financial Engineering**
- Demonstrating a strong grasp of theory combined with hands-on implementation
- Extending toward trading strategy backtesting, factor models, or credit risk modeling

---

##  Contact

Feel free to reach out for collaboration, interview inquiries, or further discussion:

- Email: nico042101@gmail.com
