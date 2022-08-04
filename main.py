# Imports and Packages

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D


# Data Visualisation with 3D Charts

def f(x, y):
    r = 3 ** (-x ** 2 - y ** 2)
    return 1 / (r + 1)


# Make our x and y data

x4 = np.linspace(start=-2, stop=2, num=200)
y4 = np.linspace(start=-2, stop=2, num=200)

# Generating 3D plot

fig = plt.figure(figsize=[16, 12])
ax = fig.gca(projection="3d")
