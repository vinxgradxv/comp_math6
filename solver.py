import math
import numpy as np
from scipy.integrate import odeint

from output_manager import print_eyler_row, print_eyler_header

def modified_eyler(data):
    x = data.x_0
    y = data.y_0
    results = []
    exact = exact_solution(data.y_0, data.l, data.r, data.h, data.func)
    n = math.trunc((data.r - data.l) / data.h) + 1
    for i in range(n):
        try:
            print_data = [i, x, y, data.func(y, x)]
            if i < math.trunc((data.r - data.l) / data.h):
                y = y + (data.h/2) * (data.func(y, x) + data.func(y + data.h * data.func(x, y), x + data.h))
            print_data.append(exact[i])
            if i < math.trunc((data.r - data.l) / data.h):
                x += data.h
            results.append(print_data)
        except Exception:
            print("Во время вычесления произошла ошибка")
            break

    return results

def runge_cutt(data):
    x = data.x_0
    y = data.y_0
    results = []
    exact = exact_solution(data.y_0, data.l, data.r, data.h, data.func)
    n = math.trunc((data.r - data.l) / data.h) + 1
    for i in range(n):
        print_data = [i, x, y, data.func(y, x)]
        k1 = data.h * data.func(y, x)
        k2 = data.h * data.func(y + k1/2, x + data.h / 2)
        k3 = data.h * data.func(y + k2/2, x + data.h / 2)
        k4 = data.h * data.func(y + k3, x + data.h)
        if i < math.trunc((data.r - data.l) / data.h):
            y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        print_data.append(exact[i])
        if i < math.trunc((data.r - data.l) / data.h):
            x += data.h
        results.append(print_data)
    return results


def adams(data):
    results = runge_cutt(data)
    n = math.trunc((data.r - data.l) / data.h) + 1
    x, y = get_x_y(results)
    f = data.func
    h = data.h
    exact = exact_solution(data.y_0, data.l, data.r, h, data.func)
    for i in range(4, n):
        k = [f(y[i - q], x[i - q]) for q in range(1, 5)]
        df = k[0] - k[1]
        d2f = k[0] - 2 * k[1] + k[2]
        d3f = k[0] - 3 * k[1] + 3 * k[2] - k[3]
        y_0 = (
                y[i - 1] +
                1 * h ** 1 * k[0] +
                1 * h ** 2 * df / 2 +
                5 * h ** 3 * d2f / 12 +
                3 * h ** 4 * d3f / 8
        )
        y[i] = y_0
        print_data = [i, x[i], y[i], data.func(y[i], x[i])]
        print_data.append(data.real_func(x[i]))
        results[i] = print_data
        for i in range(n):
            results[i][4] = exact[i]
    return results

def get_x_y(data):
    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][1])
        y.append(data[i][2])
    return x, y

def exact_solution(y0, a, b, m, func):
    t = np.arange(a, b + m, m)
    y = odeint(func, y0, t)
    ans = np.array(y).flatten()
    return ans

