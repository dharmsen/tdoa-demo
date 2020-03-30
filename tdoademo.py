# import libraries
import scipy
from scipy.optimize import fsolve
import datetime
from math import sqrt

# microphones
m0 = [-3, 0]  # coordinates of mic 0 (x,y)
m1 = [3, 1]  # coordinates of mic 1 (x,y)
m2 = [0, 4]  # coordinates of mic 2 (x,y)

v = 1503.84  # velocity of sound in saltwater at 12 degrees C

# arrival times
a0 = 15*v  # arrival time of mic 0
a1 = 11.4018*v  # arrival time of mic 1
a2 = 10*v  # arrival time of mic 2

# tdoa
t1 = a1 - a0  # tdoa between mic 0 and 1
t2 = a2 - a1  # tdoa between mic 1 and 2


def system(f):
    """
    f = [x, y] of the source location
    """
    f1 = (sqrt(((f[0]-m0[0])**2 + (f[1]-m0[1])**2)) - sqrt((f[0]-m1[0])**2 + (f[1]-m1[1])**2)) - (v*t1)
    f2 = (sqrt(((f[0]-m1[0])**2 + (f[1]-m1[1])**2)) - sqrt((f[0]-m2[0])**2 + (f[1]-m2[1])**2)) - (v*t2)
    return [f1, f2]


x = fsolve(system, [1, 1])
print(x)
