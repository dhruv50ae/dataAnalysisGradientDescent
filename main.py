# Imports and Packages

import matplotlib.pyplot as plt
import numpy as np


# First notation

def f(x):
    return x ** 2 + x + 1


# Derivative

def df(x):
    return 2 * x + 1


# Make data

x1 = np.linspace(-3, 3, 500)

# Plot function and derivative side by side

plt.figure(figsize=[10, 5])

# First Chart for f(x)

plt.subplot(1, 2, 1)
plt.grid()
plt.xlim([-3, 3])
plt.ylim([0, 8])
plt.title("Cost Function f(x)")
plt.xlabel("X")
plt.ylabel("Cost")
plt.plot(x1, f(x1))

# Second chart for df(x)

plt.subplot(1, 2, 2)
plt.grid()
plt.title("Derivative cost function df(x)")
plt.xlabel("X")
plt.ylabel("Gradient")
plt.plot(x1, df(x1))
plt.show()
