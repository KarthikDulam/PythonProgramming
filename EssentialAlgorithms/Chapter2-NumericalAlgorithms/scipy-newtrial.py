from typing import Tuple

import numpy as np
from scipy.optimize import minimize

cc1_Principal: int = 5000
cc2_Principal = 3000
cc1_min_pay = 0.02
cc2_min_pay = 0.01
cc1_rate = 0.1999
cc2_rate = 0.1099
total_pmt = 300
cc1 = [5000]
cc2 = [3000]
i = -1
j = -2


def objective(x):
    for k in range(j, i):
        print("K : " + str(k))
        cc1.append(cc1[k] + (cc1[k] * cc1_rate * 30 / 365) - x[0])
        cc2.append(cc2[k] + (cc2[k] * cc2_rate * 30 / 365) - (total_pmt - x[0]))
        print("cc1 k + 1:" + str(cc1[k+1]))
        cc1.append(cc1[k+1] + (cc1[k+1] * cc1_rate * 30 / 365) - x[1])
        cc2.append(cc2[k+1] + (cc2[k+1] * cc2_rate * 30 / 365) - (total_pmt - x[1]))
        print("cc1 k + 2:" + str(cc1[k+2]))
    return cc1[k+2] + cc2[k+2]


def constraint1(x):
    return x - (cc1[j] * cc1_min_pay)


def constraint2(x):
    return (total_pmt - x) - (cc2[j] * cc2_min_pay)


x = [150,150]
print(x)

for m in range(12):
    i = i + 2
    j = j + 2
    #print("Objective : " + str(objective(x)))
    print("i : " + str(i))
    print("j : " + str(j))
    b = (1.0, 300.0)
    bnds = (b,b)
    con1 = {'type': 'ineq', 'fun': constraint1}
    con2 = {'type': 'ineq', 'fun': constraint2}
    cons = ([con1, con2])
    solution = minimize(objective, x, method='SLSQP', bounds=bnds, constraints=cons)
    print(solution)