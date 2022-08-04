# Imports and Packages

import matplotlib.pyplot as plt
import numpy as np


# First notation

def f(x):
    return x ** 2 + x + 1


# Make data

x1 = np.linspace(-3, 3, 500)

# Plot

plt.xlim([-3, 3])
plt.ylim([0, 8])
plt.xlabel("X")
plt.ylabel("Cost")
plt.plot(x1, f(x1))
plt.show()
