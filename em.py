import matplotlib.pyplot as plt
from matplotlib import cm
import math as m

def f(x, y):
    return x**3 + y*x
    # return 3*x**2

def y(x):
    return 7*m.e**((x**2)/2) - x**2 - 2
    # return x**3 + 5

h = 0.01
x0 = 3.0
y0 = y(x0)
N = 100

X = [x0 + i*h for i in range(N)]
Y = [0 for i in range(N)]
Y[0] = y0

Y1 = [0 for i in range(N)]
Y1[0] = y0

Y2 = [0 for i in range(N)]
Y2[0] = y0

Y_real = [y(X[i]) for i in range(N)]

#Euler Method
for i in range(1, N):
    Y[i] = Y[i - 1] + h*f(X[i - 1], Y[i - 1])

#Euler Method with re
for i in range(1, N):
    y_tild = Y1[i - 1] + h*f(X[i - 1], Y1[i - 1])
    Y1[i] = Y1[i - 1] + h*(f(X[i - 1], Y1[i - 1]) + f(X[i], y_tild))/2

#Runge-Kutta 4
for i in range(1, N):
    k1 = h*f(X[i - 1], Y2[i - 1])
    k2 = h*f(X[i - 1] + h/2, Y2[i - 1] + k1/2)
    k3 = h*f(X[i - 1] + h/2, Y2[i - 1] + k2/2)
    k4 = h*f(X[i - 1] + h, Y2[i - 1] + k3)
    Y2[i] = Y2[i - 1] + (k1 + 2*k2 + 2*k3 + k4)/6

plt.plot(X, Y, X, Y1, X, Y2, X, Y_real)
plt.show()
