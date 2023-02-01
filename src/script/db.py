import pygame
import numpy as np
from math import cos, acos, sqrt, exp, sin
from time import sleep, time
from scipy import ndimage, sparse
from cvxopt import matrix, solvers
import osqp
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import random
from shapely.plotting import plot_polygon, plot_points
import matplotlib.pyplot as plt

p1 = Point(8.81, 15.81)

coords = [(8.809386930185607, 15.879693441347513), (12.31794580385132, 9.650158849015508), \
			(10.272223642428084, 8.88132253374658), (8.089822378638795, 8.766374000805232), \
			(8.809386930185607, 15.879693441347513)]
poly = Polygon(coords)

print(poly.is_valid)
print(poly.contains(p1))