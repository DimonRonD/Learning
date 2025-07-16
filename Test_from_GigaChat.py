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

print(find_adjacent(matrix_3x3))