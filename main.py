# Imports and packages

import matplotlib.pyplot as plt
import numpy as np


# A simple cost function

def f(x):
    return x ** 2 + x + 1


# Make Data

x1 = np.linspace(start=-3, stop=3, num=500)

# Plot

plt.xlim([-3, 3])
plt.ylim([0, 8])
plt.xlabel("x1")
plt.ylabel("f(x)")
plt.plot(x1, f(x1))
plt.show()
