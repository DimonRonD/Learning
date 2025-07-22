"""
60
Напишите функцию process_args, которая принимает на вход произвольное количество позиционных и именованных аргументов
и возвращает их в виде словаря.
"""
import re


def process_args(*args, **kwargs):
    my_dict = dict()
    for i, arg in enumerate(args):
        my_dict['positional_' + str(i+1)] = arg

    for el in kwargs:
        my_dict[el] = kwargs[el]

    return my_dict

"""
61
Напишите функцию multiply_string, которая принимает на вход строку text и целое число multiplier. 
Функция должна возвращать новую строку, состоящую из повторений строки text multiplier раз.
Если значение multiplier не передано, установите его по умолчанию равным 1.
"""
def multiply_string(text, multiplier):
    if multiplier is None:
        multiplier = 1
    return text * multiplier

"""
62
Напишите функцию sum_of_squares, которая принимает на вход список чисел nums и использует функцию reduce и 
лямбда-функцию для вычисления суммы квадратов всех чисел из списка.
"""
from functools import reduce
def sum_of_squares(nums):
    return reduce(lambda x, y: x + y**2, nums)

#print(sum_of_squares([1, 2, 3]))

"""
69
Создайте функцию divide_numbers, которая будет делить одно число на другое. 
Используйте блок try-except для обработки различных исключений, которые могут возникнуть при делении чисел. 
Определите, какие исключения существуют при делении чисел и учтите их при выполнении задания. 
В результате верните текст ошибки как строку.
70
Добавьте к предыдущему решению блоки else и finally.
"""
def divide_numbers(d1, d2):
    try:
        return d1 / d2
    except ZeroDivisionError as e:
        return "division by zero"
    except TypeError as e:
        return "unsupported operand type(s) for /: 'str' and 'int'"
    else:
        return "success"
    finally:
        print("finally")


"""
30
Создайте функцию validate_and_format_phones(phones), которая принимает на вход список phones с номерами телефонов.
Внутри функции пройдитесь по каждому номеру в списке phones. Проверьте, что номер соответствует следующим требованиям:
*Длина номера - 11 цифр.
+Допускается указывать "+" в начале номера.
*Допустимы разделители: ' ', '-', '(' и ')' в любом месте и количестве, кроме начала. Другие разделители не допускаются.
*Первая цифра в номере должна быть '7' или '8', другие не допускаются.
Если номер соответствует требованиям, добавьте его в результирующий список в формате +7(123)456-7890.
Если номер не соответствует требованиям, добавьте в результирующий список строку Invalid.
Верните результирующий список.
"""
import re
def validate_and_format_phones(phones):
    if phones is None:
        raise AttributeError('An attribute should not be None')
    trim = re.compile(r'(?:^\+?|[()\s-]*)')
    check = re.compile(r'(?:7|8)([0-9]{3})([0-9]{3})([0-9]{4})')
    result = []
    for el in phones:
        el = re.sub(trim,'', el)
        matched = re.match(check, el)
        if not matched:
            result.append('Invalid')
            continue
        if len(el) != 11:
            result.append('Invalid')
            continue
        if not el.startswith('7') :
            if el.startswith('8') :
                el = el.replace('8', '7', 1)
            else:
                result.append('Invalid')
                continue
        result.append('+' + el[0:1] + '(' + el[1:4] + ')' + el[4:7] + '-' + el[7:])

    return result

#print(validate_and_format_phones(['79085131035', '89515345534', '+7(906)490-33-22', '99993332211', '7$951$5345534']))

"""
31
Создайте функцию find_dates_in_text(text), которая принимает на вход текст text.
Используя регулярное выражение r, выполните поиск дат в тексте text.
Регулярное выражение r должно соответствовать датам в формате YYYY-MM-DD, где YYYY - год, MM - месяц и DD - день.
Верните список всех найденных дат в тексте.
"""
def find_dates_in_text(text):
    return re.findall(r'(\d{4}-\d{2}-\d{2})', text)

text = """
jnkjdjnwe 2024-03-54 mkwsdklmsckmkm 2025-07-22 okwdklwoksoiojqwed 2025/02/21
"""
#print(find_dates_in_text(text))

"""
32
Создайте функцию extract_url_without_scheme(web_url), которая принимает на вход строку web_url с URL-адресом.
Используя регулярное выражение r, выполните поиск схемы доступа в URL-адресе.
Удалите схему доступа из URL-адреса с помощью регулярного выражения trim.
Верните URL-адрес без указания схемы доступа.
"""
import re
def extract_url_without_scheme(web_url):
    # Регулярное выражение для удаления схем HTTP/HTTPS
    pattern = r'^https?://'

    # Используем метод sub() для замены найденной схемы на пустую строку
    trimmed_url = re.sub(pattern, '', web_url)

    return trimmed_url

