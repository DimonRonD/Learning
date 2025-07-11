"""
| День недели | Миша | Алина | Саша |
| ----------- | ---- | ----- | ---- |
| Понедельник |  7   |   8   |   5  |
| Вторник     |  6   |   7   |   4  |
| Среда       |  7   |   8   |   5  |
| Четверг     |  5   |   4   |   6  |
| Пятница     | 10   |   8   |   9  |

Используйте данные из таблицы и посчитайте, сколько времени в среднем проводят за компьютером
Миша, Алина и Саша по отдельности. Сохраните результаты в переменные time_Misha, time_Alina и time_Sasha соответственно.

Найдите среднее количество времени за компьютером среди всех трех коллег.
Запишите результат в переменную time_total. Используйте списки для решения задачи.

"""

employee = ["Миша", "Алина", "Саша"]
days = [[7, 8, 5], [6, 7, 4], [7, 8, 5], [5, 4, 6], [10, 8, 9]]

time_Misha = 0
time_Alina = 0
time_Sasha = 0


for i in range(len(employee)):
    for j in range(len(days)):
        if i == 0:
            time_Misha += days[j][i]
        elif i == 1:
            time_Alina += days[j][i]
        else:
            time_Sasha += days[j][i]

time_Misha = time_Misha / 5
time_Alina = time_Alina / 5
time_Sasha = time_Sasha / 5

time_total = round(((time_Misha + time_Alina + time_Sasha) / 3), 1)

print(time_Misha, time_Alina, time_Sasha, time_total)

