"""
49
Напишите функцию find_unique_elements, которая принимает на вход список lst и возвращает список уникальных
элементов этого списка. Используйте встроенные функции. Отсортируйте результат по возрастанию.
"""
def find_unique_elements(lst):
    return sorted(list(set(lst)))

# print(find_unique_elements([4,6,2,7,1,8,3,6]))

"""
54
Напишите функцию sums_by_quarter, которая принимает список чисел (показаний термометра с января по декабрь) и 
возвращает список сумм значений по кварталам. Каждый квартал состоит из трех месяцев, и список должен быть разбит 
на соответствующие кварталам элементы. При этом, каждый квартал должен быть представлен 
одним числом - суммой элементов в этом квартале.
"""

def sums_by_quarter(lst):
    counter = 0
    tmp = []
    temp = 0
    for item in lst:
        temp += int(item)
        counter += 1
        if counter % 3 == 0:
            tmp.append(temp)
            temp = 0
    return tmp

# print(sums_by_quarter([3, 5, 8, 12, 18, 22, 25, 28, 31, 27, 18, 12]))

"""
55
Напишите функцию sorted_unique_list, которая принимает список чисел и возвращает список, отсортированный по 
возрастанию и без повторяющихся элементов. Используйте специальную функцию.
"""

def sorted_unique_list(lst):
    return sorted(list(set(lst)))

"""
56
Напишите функцию count_frequency, которая принимает список имен (строк) и возвращает словарь, содержащий количество 
упоминаний каждого имени в списке. Словарь должен быть отсортирован по ключам в алфавитном порядке.
"""

def count_frequency(lst):
    my_dict = dict()
    for i in range(len(lst)):
        my_dict[lst[i]] = lst.count(lst[i])

    return dict(sorted(my_dict.items()))

# print(count_frequency(['sdwev', 'wefe', 'wefew', 'wefe', 'wefew', 'wefew']))


"""
58
Напишите функцию flatten_nested_list, которая принимает в качестве аргумента вложенный список (список списков) 
и возвращает плоский список, состоящий из всех элементов вложенных списков.
"""

def flatten_nested_list(lst):
    return [el for suberr in lst for el in suberr]


lst = [
    ['sdwev', 'wefe', 'wefew'],
    [1, 2, 3],
    [5, 6, 7],
]

# print(flatten_nested_list(lst))

"""
59
Напишите функцию process_commands, которая принимает на вход список команд и выполняет их. 
Каждая команда представляет собой строку, которая может быть одной из следующих: 
* execute: добавляет текущий индекс выполнения команды в список результатов; 
* skip: игнорирует команду и переходит к следующей; 
* stop: прекращает выполнение команд.
Функция process_commands должна возвращать список всех индексов выполнения команд.
"""

def process_commands(lst):
    results = []
    for i, command in enumerate(lst):
        if command == 'execute':
            results.append(i)
        elif command == 'skip':
            pass
        elif command == 'stop':
            return results

    return results


"""
35
Создайте функцию de_none(lst), которая принимает на вход список lst.
Проходите по элементам списка и проверьте, равен ли какой-либо его элемент значению None.
Если элемент списка не равен None, добавьте его в новый список res.
Верните новый список res, который не содержит значений None.
"""

def de_none(lst):
    return [el for el in lst if el is not None]

"""
36
Создайте функцию segment(num, scale), которая принимает на вход число num и список чисел scale, 
отсортированный по возрастанию. Число num выбрано случайным образом в промежутке между минимальным и 
максимальным значением в списке scale.
* Найдите минимальное и максимальное значение в списке scale.
Проверьте, является ли num соседним числом справа или слева от другого числа в списке scale, 
или совпадает с числом в списке.
*Если num соседнее слева или справа, верните кортеж из двух соседних чисел.
* Если num совпадает с числом в списке, верните кортеж из двух одинаковых чисел.
Если num не является соседним числом и не совпадает с числом в списке, верните None.
"""

def segment(num, scale):
    mini = min(scale)
    maxi = max(scale)
    if num in scale:
        return (num, num)
    for i in range(len(scale)):
        if scale[i] + 1 == num:
            return (scale[i], scale[i+1])
        elif scale[i] - 1 == num:
            return (scale[i-1], scale[i])
    return None

print(segment(5, [1,2,3,7,8,9,10]))