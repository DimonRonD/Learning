"""
63
Создайте класс Student, который будет представлять студента университета.
У студента должны быть следующие атрибуты: name, age, major и gpa.
Атрибут gpa должен иметь значение по умолчанию равное 0.

Также добавьте метод get_info, который будет выводить информацию о студенте в виде строки в следующем формате:
"Имя: {имя}, Возраст: {возраст}, Специальность: {специальность}, Средний балл: {средний_балл}".
"""
import math

"""
64
Добавьте в предыдущее задание класса Student новый метод strip_code, который будет удалять все цифры из имени студента.
"""

"""
65
Дополните предыдущее задание с классом Student, создав новый класс GraduateStudent, 
который будет наследоваться от класса Student. В классе GraduateStudent также должен быть определен конструктор, 
который будет вызывать конструктор родительского класса Student, чтобы установить имя, возраст, 
специальность и средний балл для выпускника.
"""

"""
66
Добавьте возможность переопределения методов в классе GraduateStudent, чтобы ученики могли переопределять 
метод get_info(), добавляя дополнительную информацию к выводу.
"""

class Student:
    def __init__(self, name, age, major, gpa=0):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Специальность: {self.major}, Средний балл: {self.gpa}"

    def strip_code(self):
        self.name = ''.join(char for char in self.name if not char.isdigit())

class GraduateStudent(Student):
    def __init__(self, name, age, major, gpa, education_level):
        super().__init__(name, age, major, gpa)
        self.education_level = education_level

    def get_info(self, *args):
        base_info = f"{super().get_info()}, Уровень образования: {self.education_level}"
        if args:
            additional_info = f"Дополнительная информация:"
            for arg in args:
                additional_info += ' ' + arg
        return


student1 = Student("Иван Петров", 20, "Информатика",8)
#print(student1.get_info())

student1 = Student("Иван Петров123", 20, "Информатика")
#print(f"ДО очистки: {student1.get_info()}")
student1.strip_code()
#print(f"ПОСЛЕ очистки: {student1.get_info()}")

"""
67
Создайте три класса: Rectangle, Circle и Triangle. Все эти классы должны иметь метод area, 
который будет возвращать площадь фигуры.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

