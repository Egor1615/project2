n = int(input("Введите количество строк первой матрицы: "))        # Вводим количество строк и столбцов для первой матрицы
m = int(input("Введите количество столбцов первой матрицы: "))

k = int(input("Введите количество строк второй матрицы: "))               # Вводим количество строк и столбцов для второй матрицы
h = int(input("Введите количество столбцов второй матрицы: "))

result = [[0 for _ in range(h)] for _ in range(n)]                # Создаем пустую матрицу размером n x h, заполненную нулями

print("Введите элементы первой матрицы:")                       # Вводим элементы первой матрицы
matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

print("Введите элементы второй матрицы:")              # Вводим элементы второй матрицы
matrix2 = []
for _ in range(k):
    row = list(map(int, input().split()))
    matrix2.append(row)

if m != k:                                             # Проверяем, можно ли выполнить умножение матриц
    print("Умножение матриц невозможно!")
else:
    for i in range(n):                                    # Умножаем матрицы
        for j in range(h):
            for l in range(m):
                result[i][j] += matrix1[i][l] * matrix2[l][j]

    print("Произведение матриц:")                         # Выводим результат
    for row in result:
        print(' '.join(map(str, row)))
