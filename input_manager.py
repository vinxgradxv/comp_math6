import math

from InputData import InputData

functions_str = ["y' = y + (1 + x) * y ** 2", "y' = 3 * x ** 2 * y + x ** 2 * exp(x ** 3)", "y' = cos(x) - y"]
real_func_str = ["-1/x", "x^3 * e^{x^3}/3", "(cos(x) + six(x))/2"]
l_functions = [lambda y, x: y + (1 + x) * y ** 2, lambda y, x: 3 * x ** 2 + y + x ** 2 * math.exp(x ** 3), lambda y, x: math.cos(x) - y]
real_func = [lambda x: -1/x, lambda x: x ** 3 * math.exp(x ** 3)/3, lambda x: (math.cos(x) + math.sin(x)) / 2]

def get_input_data_from_console():
    while True:
        try:
            print("Выберите уравнение:")
            print("1) " + functions_str[0])
            print("2) " + functions_str[1])
            print("3) " + functions_str[2])
            n = int(input())
            if n < 1 or n > 3:
                raise Exception()
            print("Введите x_0:")
            x_0 = float(input())
            print("Введите y_0")
            y_0 = float(input())
            print("Условие: y({:.3f}) = {:.3f}".format(x_0, y_0))
            print("Введите правую границу интервала:")
            r = float(input())
            if r <= x_0:
                raise Exception()
            print("Интервал: [{:.3f}, {:.3f}]".format(x_0, r))
            print("Введите шаг h:")
            h = float(input())
            if h <= 0:
                raise Exception()
            print("Введите желаемую точность")
            accuracy = float(input())
            if accuracy <= 0:
                raise Exception()
            return InputData(n, x_0, y_0, x_0, r, h, accuracy, l_functions[n-1], real_func[n-1], functions_str[n-1], real_func_str[n-1])
        except Exception:
            print("Ошибка ввода, попробуйте еще раз")