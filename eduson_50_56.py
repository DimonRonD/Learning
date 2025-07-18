"""
50
Напишите функцию flatten_tuple, которая принимает на вход кортеж tup, содержащий внутри себя другие кортежи (подсписки).
Функция должна вернуть список, состоящий из всех элементов подсписков.
"""
def flatten_tuple(tup):
    return [el for subarr in tup for el in subarr]

"""
51
Напишите функцию sum_positive_numbers, которая принимает список целых чисел numbers
и возвращает сумму только положительных чисел из данного списка.
"""
def sum_positive_numbers(numbers):
    x = [el for el in numbers if el > 0]
    return sum(x)

#print(sum_positive_numbers([1,2,3,4,5]))

"""
52
Напишите функцию process_array, которая принимает список целых чисел numbers и возвращает новый список, 
содержащий только положительные числа, умноженные на 2.
"""
def process_array(numbers):
    return [el*2 for el in numbers if el > 0]

#print(process_array([-1, 2, 5, -9]))

"""
53
Напишите функцию list_to_dict, которая принимает список ключей и список значений. А затем возвращает словарь, 
сформированный из этих списков. Используйте генератор списка и специальную функцию.
"""
def list_to_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

#print(list_to_dict([2, 5, 9], [-2, -5, -9]))

"""
54
Напишите функцию sum_n_dimensional_vectors, которая принимает список векторов в n-мерном пространстве 
и возвращает их сумму. Векторы представлены списками чисел одинаковой длины. Сумма векторов вычисляется покомпонентно.
"""
def sum_n_dimensional_vectors(vectors):
    return [sum(component) for component in zip(*vectors)]

"""
57
на Python не используя сторонние библиотеки напишите функцию sum_n_dimensional_vectors, которая принимает список векторов в n-мерном пространстве и возвращает их сумму. Векторы представлены списками чисел одинаковой длины. Сумма векторов вычисляется покомпонентно.
Создайте список result заполненный нулями, длина которого равна длине первого вектора.
Используйте цикл for для прохода по каждому вектору в списке vectors.
Для каждого вектора, используйте функцию map() и zip() для сложения его компонент с компонентами вектора result.
Верните результат в виде кортежа.
"""
def sum_n_dimensional_vectors(vectors):
    result = [0 for el in vectors[0]]
    for el in vectors:
        result = list(map(lambda x, y: x + y, result, el))

    # Преобразуем результат обратно в кортеж
    return tuple(result)

"""
37
Создайте функцию lim_max(nums, limit), которая принимает на вход кортеж чисел nums и ограничение limit.
Инициализируйте переменную max_value со значением -1, которая будет хранить максимальное значение, строго меньшее limit.
Пройдитесь циклом по элементам кортежа nums.
Внутри цикла проверьте каждый элемент кортежа на условие: элемент должен быть строго меньше limit и больше текущего 
значения max_value.
Если условие выполняется, обновите значение max_value на текущий элемент.
По окончанию цикла, верните значение max_value.
"""

# def lim_max(nums, limit):
#     max_value = -1
#     for el in nums:
#         if max_value <el < limit:
#             max_value = el
#     return max_value

"""
38
Решите предыдущую задачу с помощью списковых включений (list comprehensions), чтобы сделать код более кратким.
"""

def lim_max(nums, limit):
    candidates = [num for num in nums if num < limit]
    return max(candidates) if candidates else -1


"""
39
Напишите функцию check_list, которая принимает на вход переменную var и проверяет, является ли она списком.
"""
def check_list(var):
    return isinstance(var, list)

"""
40
Напишите функцию get_value_by_index, которая принимает на вход список ref_list и индекс index. 
Функция должна вернуть значение списка ref_list по указанному индексу, если список ref_list не равен None, 
является списком (а не другим типом данных) и индекс не выходит за пределы длины списка. 
В любом ином случае верните значение None.
"""

def get_value_by_index(ref_list, index):
    if ref_list is None:
        return None
    if not isinstance(ref_list, list):
        return None
    if len(ref_list) < index:
        return None
    return ref_list[index]

"""
41
Напишите функцию list_reorder, которая принимает на вход список списков list_of_lists. 
Функция должна изменить структуру списка, так чтобы элементы из вложенных списков 
стали элементами одного общего списка.
"""

def list_reorder(list_of_lists):
    return [el for subarr in list_of_lists for el in subarr]

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# print(list_reorder(a))

"""
41
Напишите функцию list_insert, которая принимает на вход список ref_list, индекс start, число num, и количество 
повторений rep. Функция должна вставить число num в список ref_list начиная с позиции start, повторяя его rep раз.
"""
def list_insert(list_of_lists, start, num, rep):
    if start >= len(list_of_lists):
        return -1
    for i in range(rep):
        list_of_lists.insert(start, num)
    return list_of_lists

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_insert(b, 5, 0, 3))

"""
43
Напишите функцию generate_values, которая принимает на вход начальное значение start и конечное значение end. 
Функция должна вернуть список значений в заданном числовом интервале от start до end (включительно).
"""
def generate_values(start, end):
    return [i for i in range(start, end + 1)]

"""
44
Даны два словаря dict1 и dict2. Напишите функцию merge_dicts, которая объединит эти два словаря в один с 
помощью оператора объединения и вернет результат.
"""
def merge_dicts(dict1, dict2):
    return dict1|dict2

"""
45
Даны два словаря dict1 и dict2. Напишите функцию merge_dicts, которая объединит эти два словаря. 
В начале результирующего словаря должны идти ключи dict1. Значения с общими ключами должны стать элементами 
общего списка в результирующем словаре. Функция merge_dicts должна вернуть результирующий словарь.
"""

def merge_dict(dict1, dict2):
    result_dict = dict1.copy()
    for key, value in dict2.items():
        if key in result_dict:
            if isinstance(result_dict[key], list):
                result_dict[key].append(value)
            else:
                result_dict[key] = [result_dict[key], value]
        else:
            result_dict[key] = value

    return result_dict

"""
46
Напишите функцию count_elements, которая принимает на вход коллекцию (список, кортеж, множество или строку) 
и возвращает словарь. В нем ключами должны быть уникальные элементы коллекции, а значениями - количество их 
вхождений в данную коллекцию. В результате верните получивышийся словарь.
"""
def count_elements(collection):
    dict = {k: 0 for k in collection}
    for el in collection:
        dict[el] += 1
    return dict

"""
47
Напишите функцию get_value, которая принимает на вход словарь data и ключ key. 
Функция должна возвращать значение из словаря data, соответствующее переданному ключу key. 
Если ключ отсутствует в словаре, функция должна возвращать строку "Key not found".
"""
def get_value(data, key):
    return data[key] if key in data else "Key not found"

"""
48
Напишите функцию sort_dict, которая принимает на вход словарь d, тип сортировки type (keywise или valuewise) 
и порядок сортировки order (asc или desc). Функция должна возвращать отсортированный словарь по ключам или значениям, 
в зависимости от переданных параметров.
"""
def sort_dict(d, type, order):
    ord = False
    if order == "desc":
        ord = True
    if type == "valuewise":
        return dict(sorted(d.items(), key=lambda item: item[1], reverse=ord))
    else:
        return sorted(d.items(), reverse=ord)
