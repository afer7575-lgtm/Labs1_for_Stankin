from func_for_test import *
from storage_to_csv import to_storage
import random

def random_list(length, low=0, high=100, integer=True):
    """
    Создаёт список случайных чисел заданной длины.

    Параметры:
        length (int): длина списка.
        low (int/float): нижняя граница диапазона (по умолчанию 0).
        high (int/float): верхняя граница диапазона (по умолчанию 100).
        integer (bool): если True, генерируются целые числа,
                        иначе — вещественные.

    Возвращает:
        list: список случайных чисел.
    """
    if integer:
        return [random.randint(low, high) for _ in range(length)]
    else:
        return [random.uniform(low, high) for _ in range(length)]

if __name__ == "__main__":
    """arr_for_test = [428, 813, 47, 952, 176, 684, 339, 871, 592, 63, 777, 241, 898, 514, 322, 699, 105, 986, 451, 738, 28, 664, 819, 377, 941, 286, 735, 178, 803, 529, 647, 92, 566, 713, 384, 829, 258, 699, 111, 908, 435, 872, 556, 191, 764, 318, 978, 443, 636, 789, 205, 857, 472, 934, 367, 600, 293, 751, 138, 826, 497, 214, 685, 399, 862, 539, 972, 116, 682, 341, 758, 229, 849, 404, 917, 576, 132, 789, 465, 812, 258, 693, 334, 979, 447, 871, 599, 213, 765, 328, 885, 541, 108, 654, 386, 721, 273, 953, 506, 169]
    func1 = first_el(arr_for_test)
    func2 = binary_search(sorted(arr_for_test), arr_for_test[10])
    func3 = linear_search(arr_for_test, arr_for_test[10])
    func4 = find_min(arr_for_test)
    func5 = buble_sort(arr_for_test)"""

    n_test = [10,50,100,500,1000,5000,10000,50000,100000,500000,1000000,5000000,10000000]
    result = []
    for n in n_test:
        arr_for_test = random_list(n)
        result_n = {
            "count": n,
            "time": str(first_el(arr_for_test)["time"]).replace("e","E").replace('.',',')
        }
        result.append(result_n)
    to_storage(result,"first_el")
    print("first_el")

    result = []
    for n in n_test:
        arr_for_test = random_list(n)
        result_n = {
            "count": n,
            "time": str(binary_search(sorted(arr_for_test), arr_for_test[-1])["time"]).replace("e","E").replace('.',',')
        }
        result.append(result_n)
    to_storage(result,"binary_search")
    print("binary_search")

    result = []
    for n in n_test:
        arr_for_test = random_list(n)
        result_n = {
            "count": n,
            "time": str(linear_search(arr_for_test, arr_for_test[-1])["time"]).replace("e","E").replace('.',',')
        }
        result.append(result_n)
    to_storage(result,"linear_search")
    print("linear_search")

    result = []
    for n in n_test:
        arr_for_test = random_list(n)
        result_n = {
            "count": n,
            "time": str(find_min(arr_for_test)["time"]).replace("e","E").replace('.',',')
        }
        result.append(result_n)
    to_storage(result, "find_min")
    print("find_min")

    result = []
    for n in [10, 100, 1000, 10000]:
        arr_for_test = random_list(n)
        result_n = {
            "count": n,
            "time": str(buble_sort(arr_for_test)["time"]).replace("e","E").replace('.',',')
        }
        result.append(result_n)
    to_storage(result, "buble_sort")
    print("buble_sort")

