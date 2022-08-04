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

# Multiple minima vs Initial guess and advanced functions

# Make some data

x2 = np.linspace(-2, 2, 1000)


# g(x) function

def g(x):
    return x ** 4 - 4 * x ** 2 + 5


# dg(x) function

def dg(x):
    return 4 * x ** 3 - 8 * x


# Plot function and derivative side by side

plt.figure(figsize=[10, 5])

# First Chart for g(x)

plt.subplot(1, 2, 1)
plt.grid()
plt.xlim([-2, 2])
plt.ylim([0, 6])
plt.title("Cost Function g(x)")
plt.xlabel("X")
plt.ylabel("Cost")
plt.plot(x2, g(x2))

# Second chart for dg(x)

plt.subplot(1, 2, 2)
plt.grid()
plt.title("Derivative cost function dg(x)")
plt.xlabel("X")
plt.ylabel("Gradient")
plt.xlim(-2, 2)
plt.ylim(-20, 20)
plt.plot(x2, dg(x2))

plt.show()


# Python loop and Gradient descent:

def gradientDescent(derivativeFunc, initialGuess, multiplier=0.02, precision=0.0001, max=300):
    newX = initialGuess

    xList = [newX]
    slopeList = [derivativeFunc(newX)]

    for n in range(max):
        previousX = newX
        gradient = derivativeFunc(previousX)
        newX = previousX - multiplier * gradient
        stepSize = abs(newX - previousX)
        xList.append(newX)
        slopeList.append(derivativeFunc(newX))

        if stepSize < precision:
            break

    return newX, xList, slopeList


localMin, listX, derivList = gradientDescent(dg, -0.1)

print(localMin)
print(len(listX))

# Divergence, overflow and tuples

# Make data

x3 = np.linspace(start=-2.5, stop=2.5, num=1000)


def h(x):
    return x ** 5 - 2 * x ** 4 + 2


def dh(x):
    return 5 * x ** 4 - 8 * x ** 3


localMin, listX, derivList = gradientDescent(dh, 0.2)

print(localMin)
print(len(listX))

plt.subplot(1, 2, 1)
plt.grid()
plt.plot(x3, h(x3))

plt.subplot(1, 2, 2)
plt.grid()
plt.plot(x3, dh(x3))

plt.show()
