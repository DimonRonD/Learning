"""
Надо создать приложение для планирования задач.
Задачи в формате строки, разделены пробелами внутри, разделены запятыми между задачами.
Формат записи: "Тело задачи с HH:MM до HH:MM <важность>".
Важность может быть "неважное, обычное, важное"
Новая запись приходит в таком же формате. Надо проверять пересечение времени и важность.
- Если важность больше и время совпадает, то заменяем запись, пишем, какую запись убрали.
- Если важность равна или меньше, то смотрим совпадение времени. Если время свободно, добавляем запись.
- Если важность равна или меньше и время занято, то пишем, что не удалось добавить запись, так как время занято.
"""
from colorama import Fore

def split_notes(remainder):
    tmp = remainder.split(',')
    splitted_notes = [repack_note(el.strip()) for el in tmp]
    return splitted_notes

def repack_note(note):
    *base, _, start_time, _, end_time, importance = note.split(' ')
    base = ' '.join(base)
    return [base, start_time, end_time, importance]

def define_time(note):
    s_hh, s_mm = note[1].split(':')
    e_hh, e_mm = note[2].split(':')
    s_hh, s_mm, e_hh, e_mm = int(s_hh), int(s_mm), int(e_hh), int(e_mm)
    s_time = s_hh * 60 + s_mm
    e_time = e_hh * 60 + e_mm
    return s_time, e_time

def delete_note(note, all_notes):
    for el in all_notes:
        if el[0] == note[0]:
            all_notes.remove(el)
    return all_notes

def add_note(note, all_notes):
    all_notes.append(note)
    return all_notes

def compare_time(all_notes, new_note):
    s_time_new, e_time_new = define_time(new_note)
    for note in all_notes:
        s_time, e_time = define_time(note)
        if ((s_time_new < e_time < e_time_new)
            or (s_time_new < s_time < e_time_new)
            or (s_time_new >= s_time and e_time_new <= e_time)
            ):
            if IMPORTANCE[new_note[3]] <= IMPORTANCE[note[3]]:
                print(Fore.RED + f"Не удалось добавить запись {new_note}, так как время занято задачей {note}" + Fore.RESET)
                return all_notes
            else:
                all_notes = delete_note(note, all_notes)
                all_notes = add_note(new_note, all_notes)
                print(Fore.GREEN + f"Удалена запись {note}\nДобавлена запись {new_note}" + Fore.RESET)
                return all_notes
    all_notes = add_note(new_note, all_notes)
    print(Fore.GREEN + f"Добавлена запись {new_note}" + Fore.RESET)
    return all_notes
    return all_notes

def print_notes(all_notes):
    printed_notes = sorted(all_notes, key=lambda note: note[1])
    for note in printed_notes:
        print(Fore.BLUE, note, Fore.RESET)

remainder = "Полить цветы с 09:30 до 10:00 обычное, приготовить завтрак и позавтракать с 11:00 до 12:00 важное, пойти на тренировку с 17:30 до 19:30 важное"
# new_remi = "Почитать книгу с 10:00 до 12:00 обычное"
# Почитать толстую книгу с 10:00 до 11:00 важное

IMPORTANCE = {"важное" : 100,
              "обычное" : 50,
              "неважное" : 10}

all_notes = split_notes(remainder)
input_note = ""
while True:
    input_note = input("Введите новую заметку (exit для выхода): ")
    if input_note.lower() == "exit":
        break
    new_note = repack_note(input_note)
    print_notes(compare_time(all_notes, new_note))

