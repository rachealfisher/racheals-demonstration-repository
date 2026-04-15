# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:26:46 2026

@author: regal
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# load in simulated "collected data"
data = np.load("dataset.npz")
t = data["t"]
EF_data = data["EF"]
ER_data = data["ER"]
GS_data = data["GS"]


# write our function dependent on time and tau values
def MVsim(t, tau1, tau2, tau3, EF0):
    N = len(t) # number of points
    
    # define our tau values
    k1 = 1/tau1 
    k2 = 1/tau2 
    k3 = 1/tau3 
    
    # create empty arrays 
    EF = np.zeros(N)
    ER = np.zeros(N)
    GS = np.zeros(N)
    
    # create a starting flat excited state population
    EF[0] = EF0
    
    # define a "dt" or a timestep between each point
    dt = 0.1

    # for each point, calculate the change in population and the new population
    for i in range(N - 1):
        # dEF, ER, GS use our rate equations 
        dEF = (-k1*EF[i] - k2*EF[i]) * dt
        EF[i+1] = EF[i] + dEF # the population after each change = the population in the state before + the change

        dER = (k2*EF[i] - k3*ER[i]) * dt
        ER[i+1] = ER[i] + dER

        dGS = (k1*EF[i] + k3*ER[i]) * dt
        GS[i+1] = GS[i] + dGS

    return EF, ER, GS # return each changing population


# let's plot our data alone to help guide our EF0 guess
plt.figure()

plt.plot(t, EF_data, label="EF data")

plt.plot(t, ER_data, label="ER data")

plt.plot(t, GS_data, label="GS data")

plt.legend()
plt.show()

# curve fit can only accept one array. Therefore, we need to concatenate all of our arrays.
# this is a wrapper function that does that for us
def model_all(t, tau1, tau2, tau3, EF0):
    EF, ER, GS = MVsim(t, tau1, tau2, tau3, EF0)
    return np.concatenate((EF, ER, GS))

ydata = np.concatenate((EF_data, ER_data, GS_data))

p0 = [4, 4, 6, 10000] # make some tau guesses

# fit to our model
popt, pcov = curve_fit(model_all, t, ydata, p0=p0)

print("Fitted taus and EF0:", popt)
EF_fit, ER_fit, GS_fit = MVsim(t, *popt) # *popt automatically unwraps all of our variables. so *popt = tau1, tau2, tau3

# let's plot our data with the fit on top
plt.figure()

plt.plot(t, EF_data, alpha=0.3, label="EF data")
plt.plot(t, EF_fit, label="EF fit")

plt.plot(t, ER_data, alpha=0.3, label="ER data")
plt.plot(t, ER_fit, label="ER fit")

plt.plot(t, GS_data, alpha=0.3, label="GS data")
plt.plot(t, GS_fit, label="GS fit")

plt.legend()
plt.show()
