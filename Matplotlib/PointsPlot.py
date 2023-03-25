
# This program takes two points as input and plots them

import matplotlib.pyplot as plt
import numpy as np

x1 = input("Enter x coordinate for first point : ")
y1 = input("Enter y coordinate for first point : ")
x2 = input("Enter x coordinate for second point : ")
y2 = input("Enter y coordinate for second point : ")

xpoints = np.array([x1, x2])
ypoints = np.array([y1, y2])

plt.plot(xpoints, ypoints, 'o')
plt.show()
