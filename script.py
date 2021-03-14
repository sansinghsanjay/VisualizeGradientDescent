import matplotlib.pyplot as plt
import numpy as np
import math

a = [150] # or 375
generate_a = []
lr = 5.0

def generate_y(x):
    y = math.sin(math.radians(x))
    return y

def make_plot(x, y, a, generate_a):
    plt.title("Simple Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.plot(x, y)
    plt.scatter(a, generate_a)
    plt.show()
    plt.close()

x = list(range(90, 450))

y = []

for i in range(len(x)):
    y.append(generate_y(x[i]))

y = list(y)

itr = 1
derivative_a = -1
while(derivative_a != 0):
    print("Iteration - ", itr, ":")
    print("a = ", a)
    generate_a.append(math.sin(math.radians(a[len(a) - 1])))
    print("sin(a) = ", generate_a)
    input("Enter a key to show plot: ")
    make_plot(x, y, a, generate_a)
    derivative_a = math.cos(math.radians(a[len(a) - 1]))
    print("Derivative of a = ", derivative_a)
    a.append(a[len(a) - 1] - (lr * derivative_a))
    print("Updated value of a = ", a)
    print("")
    itr += 1
