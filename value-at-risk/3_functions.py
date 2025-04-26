import numpy as np
from scipy.stats import chi2

# Define Kupiec Test function
def kupiec_test(exceptions, confidence_level, alpha=0.05):
    n1 = exceptions.sum()
    n = len(exceptions)
    n0 = n - n1
    q_hat = n1 / n
    q_0 = 1 - confidence_level

    LR_POF = -2 * (
        np.log((1 - q_0)**n0 * q_0**n1) -
        np.log((1 - q_hat)**n0 * q_hat**n1)
    )
    chi2_crit = chi2.ppf(1 - alpha, df=1)
    return LR_POF, chi2_crit, n1

# Define Christoffersen Test function
def christoffersen_test(exceptions, alpha=0.05):
    T = exceptions.values
    n00 = n01 = n10 = n11 = 0

    for t in range(1, len(T)):
        if T[t - 1] == 0 and T[t] == 0:
            n00 += 1
        elif T[t - 1] == 0 and T[t] == 1:
            n01 += 1
        elif T[t - 1] == 1 and T[t] == 0:
            n10 += 1
        elif T[t - 1] == 1 and T[t] == 1:
            n11 += 1

    pi01 = n01 / (n00 + n01) if (n00 + n01) > 0 else 0
    pi11 = n11 / (n10 + n11) if (n10 + n11) > 0 else 0
    pi = (n01 + n11) / (n00 + n01 + n10 + n11)

    logL_indep = 0
    if pi not in [0, 1]:
        logL_indep = (n01 + n11) * np.log(pi) + (n00 + n10) * np.log(1 - pi)

    logL_dep = 0
    if pi01 not in [0, 1] and pi11 not in [0, 1]:
        logL_dep = (
            n00 * np.log(1 - pi01) + n01 * np.log(pi01) +
            n10 * np.log(1 - pi11) + n11 * np.log(pi11)
        )

    LR_CC = -2 * (logL_indep - logL_dep)
    chi2_crit = chi2.ppf(1 - alpha, df=1)

    return LR_CC, chi2_crit

# Define function to assign multiplier based on number of exceptions
def assign_multiplier(x):
    if x <= 4:
        return 3
    elif 5 <= x < 9:
        return 3 + 0.2 * (x - 4)
    else:
        return 4

# Define function to calculate capital requirement
def calculate_capital_requirement(var_test_day, average_var, multiplier):
    max_value = np.maximum(var_test_day, average_var * multiplier)
    return -np.abs(max_value)
