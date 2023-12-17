#%%
import sys
sys.path.append('..')

import numpy as np
import matplotlib.pyplot as plt 
from src.functions import simulation
from C_code.wrapper import c_simulation

np.random.seed(250719)

#%%
N = 1000
h = 50000
# %%

# %%
output = simulation(N, h)

#%%
%timeit simulation(N, h)
# %%
mean = np.mean(output[-1])
median = np.median(output[-1])
print(f"Mean:  {mean} \nMedian {median}")

hist_mean = np.mean(output, axis=1)
hist_median = np.median(output, axis=1)

plt.plot(hist_mean, label='mean')
plt.plot(hist_median, label='median')
plt.legend()
plt.show()

#%%
vec_out = output.flatten()
# %%
