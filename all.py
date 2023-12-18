def task1():
    def print_pascals_triangle(n):
        if n < 0:
            print("please , use only positive integer numbers")
            return
        for i in range(n):
            coef = 1
            for j in range(1, n - i + 1):
                print(" ", end="")
            for j in range(0, i + 1):
                if j > 0:
                    coef = coef * (i - j + 1) // j
                print(coef, " ", end="")
            print()

    print("Enter the number (positive integer) of rows:")
    n = int(input())
    print_pascals_triangle(n)


def task2():
    def maxx_palindrome(s):  # find the longest palindrome
        maxx = ''
        for i in range(len(s)):  # go through all substrings and check if they are palindromes
            for f in range(i + 1, len(s) + 1):
                dood = s[i:f]
                if palindrome(dood) and len(dood) > len(maxx):
                    maxx = dood
        return maxx

    s = input('Enter a string of numbers: ')  # input of the string
    result = maxx_palindrome(s)
    if s.isdigit() == True:  # check if the string contains only numbers
        print('The longest palindromic string:', result)  # output of the longest palindrome
    else:
        print('This string contains not only numbers.')  # output if the string contains not only numbers
        s = input('Enter a string of numbers: ')  # input of the string


def task3():
    n = int(input("Введите количество строк первой матрицы: "))  # Вводим количество строк и столбцов для первой матрицы
    m = int(input("Введите количество столбцов первой матрицы: "))

    k = int(input("Введите количество строк второй матрицы: "))  # Вводим количество строк и столбцов для второй матрицы
    h = int(input("Введите количество столбцов второй матрицы: "))

    result = [[0 for _ in range(h)] for _ in range(n)]  # Создаем пустую матрицу размером n x h, заполненную нулями

    print("Введите элементы первой матрицы:")  # Вводим элементы первой матрицы
    matrix1 = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix1.append(row)

    print("Введите элементы второй матрицы:")  # Вводим элементы второй матрицы
    matrix2 = []
    for _ in range(k):
        row = list(map(int, input().split()))
        matrix2.append(row)

    if m != k:  # Проверяем, можно ли выполнить умножение матриц
        print("Умножение матриц невозможно!")
    else:
        for i in range(n):  # Умножаем матрицы
            for j in range(h):
                for l in range(m):
                    result[i][j] += matrix1[i][l] * matrix2[l][j]

        print("Произведение матриц:")  # Выводим результат
        for row in result:
            print(' '.join(map(str, row)))


while True:
    n = int(input('Enter the number of the problem (1-3): '))
    if n == 1:
        task1()
    if n == 2:
        task2()
    if n == 3:
        task3()