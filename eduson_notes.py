import os
from colorama import Fore, Back, Style
import tkinter as tk



# Создаем файл с заметкой
def build_note(note_text, note_name):
    try:
        with open(f"{note_name}.txt", "w", encoding="utf-8") as f:
            f.write(note_text)
        print(f"Заметка {note_name}.txt создана")
    except FileNotFoundError:
        print(Fore.RED, f"Файл {note_name} не найден")
    except OSError:
        print(Fore.RED, f"Удаление файла {note_name} не удалось. Системная ошибка")
    except Exception as error:
        print(Fore.RED, f"При создании файла {note_name} возникла ошибка {error}")

# Создаём заметку, вводим имя и содержание заметки
def create_note():
    note_name = input("Введите название файла: ")
    if note_name is None:
        print(Fore.RED, "ОШИБКА! Имя файла не может быть пустым")
        return create_note()
    note_text = input("Введите текст заметки: ")
    build_note(note_text, note_name)

def read_note():
    note_name = input("Введите название файла: ")
    try:
        with open(f"{note_name}.txt", "r", encoding="utf-8") as f:
            note_text = f.read()
        print(Fore.LIGHTWHITE_EX, f"Содержимое файла {note_name}.txt\n{note_text}")
    except FileNotFoundError:
        print(Fore.RED, f"Файл {note_name} не найден")
    except OSError:
        print(Fore.RED, f"Удаление файла {note_name} не удалось. Системная ошибка")
    except Exception as error:
        print(Fore.RED, f"При создании файла {note_name} возникла ошибка {error}")

def delete_note():
    note_name = input("Введите название файла для удаления: ")
    try:
        os.remove(f"{note_name}.txt")
        print(Fore.RED, f"Файл {note_name} успешно удалён")
    except FileNotFoundError:
        print(Fore.RED, f"Файл {note_name} не найден")
    except OSError:
        print(Fore.RED, f"Удаление файла {note_name} не удалось. Системная ошибка")

def display_notes():
    notes = [note for note in os.listdir() if note.endswith(".txt")]
    for note in notes:
        print(Fore.LIGHTWHITE_EX, "-" * 50)
        print(Fore.LIGHTWHITE_EX, note)
        print_note(note)

    print(Fore.LIGHTWHITE_EX, "-" * 50)

def print_note(note_name):
    try:
        with open(f"{note_name}", "r", encoding="utf-8") as f:
            note_text = f.read()
        print(f"{note_text}")
    except FileNotFoundError:
        print(Fore.RED, f"Файл {note_name} не найден")
    except OSError:
        print(Fore.RED, f"Удаление файла {note_name} не удалось. Системная ошибка")
    except Exception as error:
        print(Fore.RED, f"При создании файла {note_name} возникла ошибка {error}")

# def edit_note():
#     pass

def menu():
    text_menu = """
    Меню действий:
    1. Создать заметку
    2. Список заметок"
    3. Просмотр заметки"
    4. Редактирование заметки"
    5. Удаление заметки"
    0. Выход из программы
    """
    frame = tk.Frame(window, height=221, bg=LIGHT_GRAY)
    frame.pack(expand=True, fill="both")

    total_label = tk.Label(frame, text=text_menu, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
    # print(Fore.BLUE, "Меню действий: ")
    # print(Fore.BLUE, "1. Создать заметку")
    # print(Fore.BLUE, "2. Список заметок")
    # print(Fore.BLUE, "3. Просмотр заметки")
    # #print(Fore.BLUE, "4. Редактирование заметки")
    # print(Fore.BLUE, "5. Удаление заметки")
    # print(Fore.BLUE, "0. Выход из программы")

def main():
    text_menu = """
        Меню действий:
        1. Создать заметку
        2. Список заметок"
        3. Просмотр заметки"
        4. Редактирование заметки"
        5. Удаление заметки"
        0. Выход из программы
        """
    frame = tk.Frame(window, height=300, width=500, bg=LIGHT_GRAY, border=5)
    frame.pack(expand=True, fill="both")

    total_label = tk.Label(frame, text=text_menu, anchor=tk.NW, bg=LIGHT_GRAY,
                           fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
    total_label.pack(expand=True, fill='both')

    window.mainloop()
    # while True:
    #     menu()
    #     menu_selector = input("Введите номер действия: ")
    #     if menu_selector == "1":
    #         create_note()
    #     elif menu_selector == "2":
    #         display_notes()
    #     elif menu_selector == "3":
    #         read_note()
    #     # elif menu_selector == "4":
    #     #     edit_note()
    #     elif menu_selector == "5":
    #         delete_note()
    #     elif menu_selector == "0":
    #         exit()

window = tk.Tk()
window.geometry('400x800')
window.resizable(False, False)
window.title('Notes')

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
main()