# -*- coding: utf-8 -*-
"""matplotlib.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tPoGzSyxjn_iDaiCYatGwfIf32Sz5ESN
"""

import numpy as np
import matplotlib.pyplot as plt

X_data = np.random.random(1000) * 100
y_data = np.random.random(1000) * 100

plt.scatter(X_data, y_data, c="red", alpha=0.3)
plt.show()

years = [2006 + x for x in range(16)]
weights = [80,86,89,81,85,86,83,80,85,86,88,81,82,80,84,87]

plt.plot(years, weights)

x = ["C","C++","Python","MATLAB","Javascript"]
y = [45,15,8,56,99]

plt.bar(x,y)
plt.show()

explodes = [0,0,0.2,0,0]
plt.pie(y,labels=x,explode=explodes)
plt.show()

ages = np.random.normal(20,1.5,1000)
plt.hist(ages)
plt.show()

stock_a = [100,106,116,92,96]
stock_b = [102,107,99,111]
stock_c = [98,96,110,101]

plt.plot(stock_a,label="company-1")
plt.plot(stock_b,label="company-2")
plt.plot(stock_c,label="company-3")

plt.legend()