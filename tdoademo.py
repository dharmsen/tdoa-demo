# import libraries
import scipy
import numpy as np
from scipy.optimize import fsolve
import datetime
from math import sqrt

# microphones
m0 = [-3, 0]  # coordinates of mic 0 (x,y)
m1 = [3, 1]  # coordinates of mic 1 (x,y)
m2 = [0, 4]  # coordinates of mic 2 (x,y)

v = 1503.84  # velocity of sound in saltwater at 12 degrees C

# arrival times (pythagorean theorem for model with set point source as prompt)
xs = float(input('Source x: '))
ys = float(input('Source y: '))
a0 = sqrt((-3.0-xs)**2.0 + (0.0-ys)**2.0)/v  # arrival time of mic 0
a1 = sqrt((3.0-xs)**2.0 + (1.0-ys)**2.0)/v  # arrival time of mic 1
a2 = sqrt((0.0-xs)**2.0 + (4.0-ys)**2.0)/v  # arrival time of mic 2

# tdoa
t1 = a0 - a1  # tdoa between mic 0 and 1
t2 = a0 - a2  # tdoa between mic 0 and 2
t3 = a1 - a2  # tdoa between mic 1 and 2


# solving for x and y using all 3 pair combinations

def system0(z):
    x = z[0]
    y = z[1]
    f = np.zeros(2)
    f[0] = sqrt((x-m0[0])**2 + (y-m0[1])**2) - sqrt((x-m1[0])**2 + (y-m1[1])**2) - (t1*v)
    f[1] = sqrt((x-m0[0])**2 + (y-m0[1])**2) - sqrt((x-m2[0])**2 + (y-m2[1])**2) - (t2*v)
    return f


a0 = fsolve(system0, [1, 1])
print(a0)


def system1(z):
    x = z[0]
    y = z[1]
    f = np.zeros(2)
    f[0] = sqrt((x-m0[0])**2.0 + (y-m0[1])**2.0) - sqrt((x-m1[0])**2.0 + (y-m1[1])**2.0) - (t1*v)
    f[1] = sqrt((x-m1[0])**2.0 + (y-m1[1])**2.0) - sqrt((x-m2[0])**2.0 + (y-m2[1])**2.0) - (t3*v)
    return f


a = fsolve(system1, [1, 1])
print(a)


def system2(z):
    x = z[0]
    y = z[1]
    f = np.zeros(2)
    f[0] = sqrt((x-m0[0])**2.0 + (y-m0[1])**2.0) - sqrt((x-m2[0])**2.0 + (y-m2[1])**2.0) - (t2*v)
    f[1] = sqrt((x-m1[0])**2.0 + (y-m1[1])**2.0) - sqrt((x-m2[0])**2.0 + (y-m2[1])**2.0) - (t3*v)
    return f


a = fsolve(system2, [1, 1])
print(a)

