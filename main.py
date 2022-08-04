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

# Python loop and Gradient descent:

newX = 3
previousX = 0
stepMultiplier = 0.1
precision = 0.0001

xList = [newX]
slopeList = [df(newX)]

for n in range(500):
    previousX = newX
    gradient = df(previousX)
    newX = previousX - stepMultiplier * gradient
    stepSize = abs(newX - previousX)
    xList.append(newX)
    slopeList.append(df(newX))

    if stepSize < precision:
        break

print(f"Local Minimum at: {newX}")
print(f"Slope at this point is {df(newX)}")
print(f"Cost at this point is {f(newX)}")

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

values = np.array(xList)
plt.scatter(xList, f(values), color="red", alpha=0.5)

# Second chart for df(x)

plt.subplot(1, 2, 2)
plt.grid()
plt.title("Derivative cost function df(x)")
plt.xlabel("X")
plt.ylabel("Gradient")
plt.plot(x1, df(x1))

plt.scatter(xList, slopeList, color="red", alpha=0.5)

plt.show()
