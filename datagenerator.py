import numpy as np

# MVsim function based off of rate equations
def MVsim(t, tau1, tau2, tau3):
    N = len(t)

    k1 = 1/tau1 
    k2 = 1/tau2 
    k3 = 1/tau3 

    EF = np.zeros(N)
    ER = np.zeros(N)
    GS = np.zeros(N)

    EF[0] = 10000

    dt = 0.1

    for i in range(N - 1):
        dEF = (-k1*EF[i] - k2*EF[i]) * dt
        EF[i+1] = EF[i] + dEF

        dER = (k2*EF[i] - k3*ER[i]) * dt
        ER[i+1] = ER[i] + dER

        dGS = (k1*EF[i] + k3*ER[i]) * dt
        GS[i+1] = GS[i] + dGS

    return EF, ER, GS


N = 1000
t = np.linspace(0, 0.01*(N-1), N) # create x axis values 

true_params = (5, 5, 8) # tau1, tau2, tau3

EF, ER, GS = MVsim(t, *true_params) # get our EF, ER, GS arrays of population over time with these taus

noise_level = 200 # pick a noise level

EF_noisy = EF + np.random.normal(0, noise_level, EF.shape) # add the noise to our data
ER_noisy = ER + np.random.normal(0, noise_level, ER.shape)
GS_noisy = GS + np.random.normal(0, noise_level, GS.shape)

np.savez("dataset.npz", t=t, EF=EF_noisy, ER=ER_noisy, GS=GS_noisy) # save it as an npz

print("Done")