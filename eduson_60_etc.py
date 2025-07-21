"""
60
Напишите функцию process_args, которая принимает на вход произвольное количество позиционных и именованных аргументов
и возвращает их в виде словаря.
"""

def process_args(*args, **kwargs):
    my_dict = dict()
    for i, arg in enumerate(args):
        my_dict['positional_' + str(i+1)] = arg

    for el in kwargs:
        my_dict[el] = kwargs[el]

    return my_dict
