"""
Есть список спортсменов, которым судьи поставили оценки. Это строка, где через запятую идут фамилия спортсмена и оценки.
Надо вывести этот список в виде "Фамилия,<средняя оценка>", отсортировав по оценке
выдать тех, у которых средняя 5 и более, отсортировать по оценке по убыванию,
если у кого-то одинаковая оценка, то доп.сортировать по алфавиту
"""

def split_list(sportsmens):
    sportsmens_list = []
    tmp = 0
    for el in sportsmens.strip().split("\n"):
        name, *b = el.split(',')
        for bb in b:
            tmp += int(bb)
        sportsmens_list.append([name, tmp])
        tmp = 0
    return sportsmens_list


sportsmens = """
Иванов,5,8,9,0,3
Петров,1,6,8,9,0
Сидоров,6,3,7,8,9
Бубка,9,8,7,5,6
Кудамов,6,3,7,8,9
Тудамов,6,3,7,8,9
Сюдамов,6,3,7,8,9
"""

sportsmens_list = split_list(sportsmens)
sorted_pairs = sorted(sportsmens_list, key=lambda x: (-x[1], x[0]), reverse=False)
print(sorted_pairs)
