# Imports and packages

import matplotlib.pyplot as plt
import numpy as np


# A simple cost function

def f(x):
    return x ** 2 + x + 1


# Make Data

x1 = np.linspace(start=-3, stop=3, num=500)


# Plot

# plt.xlim([-3, 3])
# plt.ylim([0, 8])
# plt.xlabel("x1")
# plt.ylabel("f(x)")
# plt.plot(x1, f(x1))
# plt.show()


# Slope and Derivatives

def df(x):
    return 2 * x + 1


# Plot function and derivative side by side
#
# plt.figure(figsize=[10, 5])
#
# # 1st Chart: Cost function
#
# plt.subplot(1, 2, 1)
# plt.xlim([-3, 3])
# plt.ylim([0, 8])
# plt.xlabel("x1")
# plt.ylabel("f(x)")
# plt.plot(x1, f(x1))
#
# # 2nd Chart: Derivative
#
# plt.subplot(1, 2, 2)
# plt.xlabel("x1")
# plt.ylabel("df(x)")
# plt.grid()
# plt.xlim([-2, 3])
# plt.ylim([-3, 6])
# plt.plot(x1, df(x1))
# plt.show()

# Python Loops and Gradient Descent

newX = 3
previousX = 0
stepMultiplier = 0.1
precision = 0.0001

xList = [newX]
slopeList = [df(newX)]

for n in range(200):
    previousX = newX
    gradient = df(previousX)
    newX = previousX - stepMultiplier * gradient
    stepSize = abs(newX - previousX)
    xList.append(newX)
    slopeList.append(df(newX))
    if stepSize < precision:
        break

print(f"Local minimum is at {newX}, {df(newX)}, {f(newX)}")

# Superimpose the gradient descent calculations on plot

plt.figure(figsize=[10, 5])
plt.subplot(1, 2, 1)
plt.xlim([-3, 3])
plt.ylim([0, 8])
plt.xlabel("x1")
plt.ylabel("f(x)")
plt.plot(x1, f(x1))

values = np.array(xList)
plt.scatter(xList, f(values), color="red", alpha=0.5)

plt.subplot(1, 2, 2)
plt.xlabel("x1")
plt.ylabel("df(x)")
plt.grid()
plt.xlim([-2, 3])
plt.ylim([-3, 6])
plt.plot(x1, df(x1))

plt.scatter(xList, slopeList, color="red", alpha=0.5)

plt.show()
