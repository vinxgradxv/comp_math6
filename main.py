from input_manager import get_input_data_from_console
from solver import modified_eyler, runge_cutt, adams
from output_manager import print_eyler, print_runge_cutt, print_graph, print_adams

if __name__ == '__main__':
    data = get_input_data_from_console()
    real_save_h = data.h
    save_h = data.h
    results = None

    print("----------------------------------------")
    print("Усовершенствованный метод Эйлера")
    while True:
        try:
            print("----------------------------------------")
            results = modified_eyler(data)
            data.h = data.h / 2
            results_for_runge = modified_eyler(data)
            r = abs((results[len(results) - 1][2] - results_for_runge[len(results_for_runge) - 1][2]) / 3)
            data.h = save_h

            print("Текущий шаг = {:.5f}".format(data.h))
            print("Желаемая точность = {:.5f}".format(data.acc))
            print("По Рунге = {:.5f}".format(r))

            if r >= data.acc:
                print("Желаемая точность не была достигнута")
                raise Exception()
            break
        except Exception:
            data.h = data.h / 2
            save_h = data.h
            if data.h <= 0.001:
                print("Невозможно добиться нужно точности с помошью этого метода")
                results = None
                break
            print("Шаг уменьшен до", data.h)

    if results is not None:
        print_eyler(results)
        print_graph(results, data, data.func_str, data.real_func_str, "Модифицированный метод Эйлера")

    print("----------------------------------------")
    print("Метод Рунге-Кутта 4 порядка")
    data.h = real_save_h
    save_h = data.h
    results = None
    while True:
        try:
            print("----------------------------------------")
            results = runge_cutt(data)
            data.h = data.h / 2
            results_for_runge = runge_cutt(data)
            r = abs((results[len(results) - 1][2] - results_for_runge[len(results_for_runge) - 1][2]) / 3)
            data.h = save_h

            print("Текущий шаг = {:.5f}".format(data.h))
            print("Желаемая точность = {:.5f}".format(data.acc))
            print("По Рунге = {:.5f}".format(r))

            if r >= data.acc:
                print("Желаемая точность не была достигнута")
                raise Exception()
            break
        except Exception:
            data.h = data.h / 2
            save_h = data.h
            if data.h <= 0.001:
                print("Невозможно добиться нужно точности с помошью этого метода")
                results = None
                break
            print("Шаг уменьшен до", data.h)

    if results is not None:
        print_runge_cutt(results)
        print_graph(results, data, data.func_str, data.real_func_str, "Метод Рунге-Кутта")

    print("----------------------------------------")
    print("Метод Адамса")
    data.h = real_save_h
    results = None
    while True:
        try:
            print("----------------------------------------")
            results = adams(data)
            r = -1
            for result in results:
                if r < abs(result[2] - result[4]):
                    r = abs(result[2] - result[4])

            print("Текущий шаг = {:.5f}".format(data.h))
            print("Желаемая точность = {:.5f}".format(data.acc))
            print("Действительная точность = {:.5f}".format(r))

            if r >= data.acc:
                print("Желаемая точность не была достигнута")
                raise Exception()
            break
        except Exception:
            data.h = data.h / 2
            save_h = data.h
            if data.h <= 0.001:
                print("Невозможно добиться нужно точности с помошью этого метода")
                results = None
                break
            print("Шаг уменьшен до", data.h)

    if results is not None:
        print_adams(results)
        print_graph(results, data, data.func_str, data.real_func_str, "Метод Адамса")

