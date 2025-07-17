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
