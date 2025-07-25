"""
Tеперь, когда волшебники определились с днем, в который они проникнут в Гринготтс, им необходимо распределить
задачи между собой. Гермиона составила список задач:
    Приготовить зелье невидимости.
    Собрать вещи и подготовить снаряжение.
    Раздобыть оборотное зелье.
Чтобы распределить задачи честно, Гермиона заколдовала три стакана с водой. Если дотронуться до стакана волшебной
палочкой, вода в нем поменяет цвет. Каждому цвету соответствует своя задача:
— если цвет окажется красным, то волшебник займется первой задачей;
— если цвет окажется синим, то волшебник займется второй задачей;
— если цвет окажется зеленым, то волшебник займется третьей задачей;
— если волшебнику выпадет любой другой цвет, значит, заклинание сработало некорректно.
Напишите программу, которая поможет волшебникам определить, какой задачей им нужно заняться.
Создайте функцию task_check(), которая принимает на вход строку с названием цвета. Цвета передаются на английском языке.
Функция должна вернуть номер задачи, которой соответствует цвет, или ноль, если цвету не соответствует ни одна задача.
"""

def task_check(text):
    if text == "red":
        return 1
    elif text == "green":
        return 3
    elif text == "blue":
        return 2
    else:
        return 0


"""
Гермионе выпала первая задача — она должна приготовить зелье невидимости. У этого зелья несложный рецепт, 
но нужно быть очень внимательной.
Гермионе нужно помешивать зелье конкретное количество раз, чтобы оно получилось правильным. 
Она помечает все помешивания на пергаменте. Общее количество помешиваний должно соответствовать одному из условий:
— делится на 4 и не делится на 100;
— делится на 400.
Напишите функцию potion_check(), которая проверит, помешала ли Гермиона зелье правильное количество раз. 
Она должна принимать на вход один аргумент — число, которое обозначает, сколько раз Гермиона помешала зелье. 
В качестве результата работы функции верните yes, если количество помешиваний верное, или no в обратном случае. 
Используйте операторы and и or, чтобы скомбинировать несколько условий в одном if.
"""
def potion_check(count):
    if (count % 4 == 0 and count % 100 != 0) or (count % 400 == 0):
        return "yes"
    else:
        return "no"


"""
Рону досталась вторая задача — собрать вещи и подготовить снаряжение. Рон составил список необходимых вещей:
— мантия-невидимка;
— волшебная палочка;
— набор зелий;
— карта;
— оберег от проклятий.
Рон не очень внимательный и боится забыть что-то важное и взять что-то лишнее. 
Помогите ему — создайте функцию importance_check(), которая проверит, нужно ли брать предмет с собой. 
Она принимает на вход один аргумент — название предмета, который можно взять. 
Названия предметов передаются на русском языке, все необходимые предметы называются так же, 
как они названы в списке выше. Если предмет входит в список и его нужно взять, верните 1. 
Если не входит — значит, брать его не нужно, верните 0.
"""

def importance_check(text):
    if text == "мантия-невидимка" or text == "волшебная палочка" or text == "набор зелий" or text == "карта" or text == "оберег от проклятий":
        return 1
    else:
        return 0


"""
Гарри досталась третья задача — приготовить оборотное зелье. Заготовку для зелья достать не составило труда, 
но чтобы оно сработало верно, Гарри необходим волос одного студента Дурмстранга. 
Студенты Дурмстранга близки к Темному Лорду, поэтому такая маскировка поможет проникнуть в Гринготтс. 
Помогите Гарри найти подходящего человека.

Известно, что фамилии всех студентов Дурмстранга в Лютном переулке оканчиваются "ов". 
Создайте функцию student_suspect(), которая определит, подходящая ли фамилия у предполагаемого студента. 
Функция принимает на вход один аргумент — строку с фамилией студента. Если фамилия оканчивается на "ов", 
верните «Лови!». В любом ином случае верните «Пропусти его».
"""

def student_suspect(text):
    return "Лови!" if text.endswith("ов") else "Пропусти его"


#print(student_suspect("Градов"))

"""
Подготовка не прошла даром — Гарри, Рону и Гермионе удалось проникнуть в Гринготтс. Они спустились к хранилищам 
и оказались в просторной комнате, в которой есть семь дверей. Только одна из них безопасная, 
за остальными скрываются ловушки.

На каждой двери есть номер из четырех цифр. Если номер является палиндромом, то дверь безопасна. 

Палиндром — это строка, которая одинаково читается в обоих направлениях. Например, строка «1331» — это палиндром.
Напишите функцию security_check(), которая проверит, безопасно ли выходить через определенную дверь. 
Функция принимает один аргумент — строку с последовательностью цифр на двери. Проверьте, является ли строка палиндромом. 
Если да, то верните «Безопасно». В любом ином случае верните «Ловушка».
"""

def security_check(text):
    ch = False
    for i in range(int(len(text)/2)):
        print(i, len(text))
        if text[i] == text[len(text) - i - 1]:
            ch = True
        else:
            return "Ловушка"
    if ch:
        return "Безопасно"


#print(security_check("235432"))


"""
Благодаря вам Гарри, Рон и Гермиона успешно проникли в Гринготтс, добыли крестраж и избежали ловушек. 
Отличная работа! Осталась последняя, но не менее сложная миссия — сбежать из Гринготтса. В этом волшебникам 
поможет дракон, который охраняет банк.
На ошейнике дракона есть кодовый замок, код к нему состоит из 4-х цифр. Чтобы он открылся, сумма всех цифр должна 
делиться на 7. К сожалению, замок заело — волшебники могут изменить только одну цифру.
Создайте функцию cipher(), которая определит, какую цифру нужно ввести волшебникам в четвертом слоте замка. 
Она принимает на вход три аргумента — три цифры, которые уже введены в кодовый замок. В результате работы функции 
верните ту цифру, которую волшебникам нужно ввести в оставшийся слот. Если никакая цифра не подходит, 
замок взломать нельзя. В таком случае верните 0.
"""

def cipher(a, b, c):
    for i in range(10):
        if (a + b + c + i) % 7 == 0:
            return i
    return 0

print(cipher(41, 25, 378))