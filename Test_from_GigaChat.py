def find_adjacent(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Проходим по каждому элементу матрицы
    for i in range(rows):
        for j in range(cols):
            current_value = matrix[i][j]

            # Проверяем правую соседнюю ячейку (если существует)
            if j + 1 < cols and matrix[i][j + 1] == current_value:
                return f"Совпадение найдено! Элементы {current_value} находятся рядом."

            # Проверяем нижнюю соседнюю ячейку (если существует)
            if i + 1 < rows and matrix[i + 1][j] == current_value:
                return f"Совпадение найдено! Элементы {current_value} находятся рядом."

    return "Совпадений не обнаружено."


# Тестовая матрица 3x3
matrix_3x3 = [
    [1, 2, 3],
    [4, 5, 5],  # Здесь соседи 5 и 5
    [7, 8, 9]
]

#print(find_adjacent(matrix_3x3))

def greet_user():
    """Запрашивает имя пользователя и выводит приветствие."""
    # Запрашиваем ввод имени пользователя
    user_name = input("Введите ваше имя: ")

    # Запрашиваем возраст пользователя
    age = input("Введите ваш возраст: ")

    try:
        # Приводим возраст к целочисленному типу
        age_int = int(age)
    except ValueError:
        # Если введён неверный формат возраста, выводим ошибку
        print("Ошибка ввода возраста.")
        return

    # Формируем приветственное сообщение
    greeting_message = f"Привет, {user_name}! Тебе {age_int} лет."

    # Выводим приветствие в консоль
    print(greeting_message)


# Демонстрационный запуск функции
if __name__ == "__main__":
    greet_user()