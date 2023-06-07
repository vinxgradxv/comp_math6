import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def print_eyler_header():
    header = " " * 14 + "i" + " " * 12 + "x_i" + " " * 12 + "y_i" + " " * 8 + "f(x, y)" + " " * 8 + "т. реш."
    print(header)

def print_eyler_row(data):
    row = " " * (15 - len(str(data[0]))) + str(data[0])

    for i in range(1, len(data)):
        row += " " * (15 - len("{:.5f}".format(data[i]))) + "{:.5f}".format(data[i])
    print(row)

def print_eyler(results):
    print_eyler_header()
    for data in results:
        print_eyler_row(data)

def print_runge_cutt(results):
    print_eyler_header()
    for data in results:
        print_eyler_row(data)


def print_graph(results, data, func, real_func, method_title):
    x_ex = np.arange(data.l, data.r + 0.01, 0.01)
    y = odeint(data.func, data.y_0, x_ex)
    y_ex = np.array(y).flatten()
    x, y = get_x_y_calced_func(results)
    plt.title(f"{method_title}\n{func}")
    plt.plot(x_ex, y_ex, 'blue', label=f"y = {real_func}")
    plt.plot(x, y, 'go--', label="Численное решение")
    plt.legend()
    plt.show()

def get_x_y_real_func(data):
    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][1])
        y.append(data[i][2])
    return x, y


def get_x_y_calced_func(data):
    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][1])
        y.append(data[i][2])
    return x, y

def print_adams(results):
    print_eyler_header()
    for data in results:
        print_eyler_row(data)

def exact_solution(y0, a, b, m, func):
    t = np.arange(a, b + m, m)
    y = odeint(func, y0, t)
    ans = np.array(y).flatten()
    return ans
