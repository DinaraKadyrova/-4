"""Вводятся 2 константы N и K. Программа,вычисляет выражение: ((К*A)*F+ K* F^T. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Матрица F Формируется следующим образом: если в подматрице С количество чисел, больших К в нечетных столбцах в области 3 больше, чем произведение чисел в нечетных строках в области 2,
то поменять в подматрице В симметрично области 1 и 3 местами, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*F+ K* F T . Выводятся по мере формирования А, F и все матричные операции последовательно
"""
import random
import time


def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()


print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q > 100:
        row_q = int(input(
            "Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))
    start = time.time()
    A, F, FA, AT = [], [], [], []  # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        FA.append([0] * row_q)
        AT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):  # заполняем матрицу А
        for j in range(row_q):
            #A[i][j] = random.randint(-5,5)
            if i < j and j < row_q - 1 - i:
                A[i][j] = 1
            elif i < j and j > row_q - 1 - i:
                A[i][j] = 2
            elif i > j and j > row_q - 1 - i:
                A[i][j] = 3
            elif i > j and j < row_q - 1 - i:
                A[i][j] = 4

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    for i in range(row_q):  # F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    C = []  # задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):  # формируем подматрицу С
        for j in range(size):
            C[i][j] = F[size+i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(C, "C", time_next - time_prev)

    count4 = 0
    count1 = 0
    for i in range(size):  # обрабатываем подматрицу С
        for j in range(i + 1, size, 1):
            if j % 2 == 1 and j < size - 1 - i and C[i][j] == 0:
                count4 += 1
            elif j % 2 == 0 and j < size - 1 - i and C[i][j] == 0:
                count1 += 1
            # print_matrix(C, "C", time_next - time_prev)

    if count4 > count1:
        for i in range(1, size // 2, 1):  # меняем подматрицу С
            for j in range(size - 1, i, -1):
                C[i][j], C[j][i] = C[j][i], C[i][j]
        for i in range(size // 2, size, 1):
            for j in range(size // 2, i, 1):
                C[i][j], C[j][i] = C[j][i], C[i][j]
        print_matrix(C, "C", time_next - time_prev)
        for i in range(size):  # формируем матрицу F
            for j in range(size):
                F[i][size - row_q % 2 + j] = C[i][j]
        print_matrix(F, "F!", time_next - time_prev)

    else:
        for j in range(row_q // 2):
            for i in range(row_q // 2):
                F[i][j], F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j] = F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j], F[i][j]

    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)
    print_matrix(A, "A", 0)

    for i in range(row_q):  # F*A
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s = s + A[i][m] * F[m][j]
            FA[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(FA, "F*A", time_next - time_prev)

    for i in range(row_q):  # AT
        for j in range(i, row_q, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)

    for i in range(row_q):  # K*AT
        for j in range(row_q):
            A[i][j] = K * AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "K*A^T", time_next - time_prev)

    for i in range(row_q):  # (F*A)-(K*AT)
        for j in range(row_q):
            FA[i][j] = FA[i][j] - A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FA, "(K*A)*F+K*F^T", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")

# except ValueError:
#    print("\nэто не число")

except FileNotFoundError:
    print(
        "\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
