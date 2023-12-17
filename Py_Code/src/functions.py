#%%
import numpy as np

#%%
def simulation(N, h, exp=False):
    output = np.empty([h, N])

    output[0] = 1
    for i in range(1, h):
        mult = np.exp(abs(np.random.normal(0, 0.01, N))) if exp else abs(np.random.normal(1, 0.01, N))
        output[i] = output[i-1] * mult

    return output