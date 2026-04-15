# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:45:03 2026

@author: regal
"""
# imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

''' generate fake data '''
# create an x-axis ranging from 0-20
x = np.arange(0, 21)

# create y data
y = 2 * x + 3

# add noise
noise_level = 3
y_noisy = y + np.random.normal(0, noise_level, 21)

# first, we should plot our fake data to see what it looks like
plt.figure()
plt.scatter(x,y_noisy, label= "data")
plt.legend()
plt.show()


# create a function. remember, the output should be = y
def line_function(x, m, b):
    return m * x + b


p0 = [1, 1]  # initial guesses
popt, pcov = curve_fit(line_function, x, y_noisy, p0=p0) # curve_fit(function, x, y, guesses)
m_fit, b_fit = popt # popt = ?
print(f"fitted m, b = {m_fit}, {b_fit}") # print your outputs if you want

y_fitted = line_function(x, m_fit, b_fit)

# let's plot our fake data again with our fit over it
plt.figure()
plt.scatter(x,y_noisy, label= "data")
plt.plot(x, y_fitted, label="fit")
plt.legend()
plt.show()