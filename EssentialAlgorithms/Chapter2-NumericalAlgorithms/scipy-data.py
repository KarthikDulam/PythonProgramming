import numpy as np
from scipy.optimize import minimize

cc1_Principal: int = 5000
cc2_Principal = 1000
cc1_min_pay = 0.02
cc2_min_pay = 0.01
cc1_rate = 0.1999
cc2_rate = 0.1099
total_pmt = 300


def objective(x):
    cc1 = []
    cc2 = []
    cc1.append(cc1_Principal + (cc1_Principal * cc1_rate * 30 / 365) - x[0])
    cc2.append(cc2_Principal + (cc2_Principal * cc2_rate * 30 / 365) - x[0])
    for i in range(35):
        cc1.append(cc1[i] + (cc1[i] * cc1_rate * 30 / 365) - x[i + 1])
    for i in range(35):
        cc2.append(cc2[i] + (cc2[i] * cc2_rate * 30 / 365) - (total_pmt - x[i + 1]))
    return cc1[35] + cc2[35]


def constraint1(x):
    cc1 = []
    cc1.append(cc1_Principal + (cc1_Principal * cc1_rate * 30 / 365) - x[0])
    for i in range(35):
        cc1.append(cc1[i] + (cc1[i] * cc1_rate * 30 / 365) - x[i + 1])
        return cc1[i] * cc1_min_pay - x[i]


def constraint2(x):
    cc2 = []
    cc2.append(cc2_Principal + (cc2_Principal * cc2_rate * 30 / 365) - x[0])
    for i in range(35):
        cc2.append(cc2[i] + (cc2[i] * cc2_rate * 30 / 365) - (total_pmt - x[i + 1]))
        return cc2[i] * cc2_min_pay - (total_pmt - x[i])


def constraint3(x):
    for i in range(35):
        return x[i] - total_pmt


x0 = []

for i in range(36):
    x0.append(150)

print(x0)
print(objective(x0))

b = (1.0, 300.0)
bnds = (b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b)
con1 = {'type': 'eq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
con3 = {'type': 'eq', 'fun': constraint3}
cons = ([con1, con2, con3])
solution = minimize(objective, x0, method='SLSQP', \
                    bounds=bnds, constraints=cons)
print(solution)
