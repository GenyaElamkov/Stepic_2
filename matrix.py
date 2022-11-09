import numpy as np


def test():
    """Выводим матрицу"""
    n = 8
    matrix = [[0] * n for _ in range(n)]  # Инициализируем матрицу 8*8

    for i in range(n):
        matrix[i][i] = 1  # Заполняем главную диагональ
        matrix[i][n - i - 1] = 2  # Заполняем побочную диагональ

    for r in range(n):  # Выводим матрицу
        for c in range(n):
            print(str(matrix[r][c]).ljust(2), end=' ')
        print()

    # matrix = []
    # for i in range(n):
    #     temp = [input() for _ in range(m)]
    #     matrix.append(temp)


def inset_matrix(n, m):
    return [[input() for _ in range(m)] for _ in range(n)]


def output_matrix_1(matrix, n, m, rev=True):
    if not rev:
        n, m = m, n

    for row in range(n):
        for col in range(m):
            if not rev:
                print(matrix[col][row], end=' ')
            else:
                print(matrix[row][col], end=' ')
        print()


def output_matrix_2():
    n, m = int(input()), int(input())
    matrix = inset_matrix(n, m)
    output_matrix_1(matrix, n, m)
    print(' ')
    output_matrix_1(matrix, n, m, False)


def matrix_trace():
    # matrix = []
    # for i in range(n):
    #     temp = [int(num) for num in input().split()]
    #     matrix.append(temp)

    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]
    res = sum([matrix[i][i] for i in range(n)])
    print(res)
    # res = 0
    # for i in range(int(input())):
    #     res += int(input().split()[i])
    # print(res)


def more_average():
    n = int(input())
    # matrix = [[int(num) for num in input().split()] for _ in range(n)]
    res = []
    for i in range(n):
        tmp = [int(num) for num in input().split()]
        aver = sum(tmp) / len(tmp)
        largest = len([num for num in tmp if num > aver])
        res.append(largest)
    print(*res, sep='\n')


def max_area_1():
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]

    arr = [matrix[i][i - j] for i in range(n) for j in range(i + 1)]
    print(max(arr))


def max_area():
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]
    arr = []
    for i in range(n):
        for j in range(n):
            if i == j:
                arr.append(matrix[i][j])
            elif j == n - i - 1:
                arr.append(matrix[i][j])
            elif i > j and (i < n - 1 - j):
                arr.append(matrix[i][j])
            elif i < j and (i > n - 1 - j):
                arr.append(matrix[i][j])

    print(max(arr))


#
# largest = matrix[0][0]
#
# for i in range(n):
#     for j in range(n):
#         if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
#             if matrix[i][j] > largest:
#                 largest = matrix[i][j]
#
# print(largest)

def sums_quarters():
    n = int(input())
    matrix = [[int(col) for col in input().split()] for _ in range(n)]
    output = [['Верхняя четверть:', 0],
              ['Правая четверть:', 0],
              ['Нижняя четверть:', 0],
              ['Левая четверть:', 0]]

    for i in range(n):
        for j in range(n):
            if i < j and (i < n - 1 - j):
                output[0][1] += matrix[i][j]
            elif i < j and (i > n - 1 - j):
                output[1][1] += matrix[i][j]
            elif i > j and (i > n - 1 - j):
                output[2][1] += matrix[i][j]
            elif i > j and (i < n - 1 - j):
                output[3][1] += matrix[i][j]

    for i in range(4):
        print(*output[i])


def multiplication_table():
    n, m = int(input()), int(input())
    matrix = [[i * j for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()


def maximum_table():
    n, m = int(input()), int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]

    latest = min(matrix[0])
    resout = 0
    for i in range(n):
        res_max = max(matrix[i])
        if latest < res_max:
            latest = res_max
            resout = f'{i} {matrix[i].index(latest)}'

    print(resout)


def column_swapping():
    n, m = int(input()), int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]
    swap = [int(i) for i in input().split()]

    for row in range(n):
        matrix[row][swap[0]], matrix[row][swap[1]] = matrix[row][swap[1]], matrix[row][swap[0]]
        for col in range(m):
            print(matrix[row][col], end=' ')
        print()


def symmetric_matrix():
    n = int(input())
    matrix = [[int(col) for col in input().split()] for _ in range(n)]
    flag = True
    for i in range(n):
        for j in range(n):
            if i < j or i > j:
                if matrix[i][j] != matrix[j][i]:
                    flag = False
                    break
    if flag:
        print('YES')
    else:
        print('NO')


def exchange_diagonals():
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]

    # Меняем местами диагонали матрицы
    for i in range(n):
        matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

    # Вывод матрицы
    for row in matrix:
        print(*row)


def mirroring():
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]

    for i in range(1, n):
        matrix[i - 1], matrix[-i] = matrix[-i], matrix[i - 1]
        if n // 2 == i:
            break

    for row in matrix:
        print(*row)


def matrix_rotation():
    """
3
1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3
    """
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]
    matrix = [reversed([matrix[j][i] for j in range(n)]) for i in range(n)]

    for row in matrix:
        print(*row)


def knight_move():
    # Координаты коня.
    cordinat = input()
    horizont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    h = ''
    if cordinat[0] in horizont:
        h = horizont.index(cordinat[0])
    v = int(cordinat[1])

    # Инициализируем доску.
    n = 8
    matrix = [['.'] * n for _ in range(n)]

    # Ход коня.
    for x in range(1, n + 1):
        for y in range(n):
            if (h - y) ** 2 + (v - x) ** 2 == 5:
                matrix[-x][y] = '*'
    matrix[-v][h] = 'N'

    # Вывод доски.
    for row in matrix:
        print(*row)


def magic_square():
    # Ввод матрицы.
    n = int(input())
    matrix = [[int(j) for j in input().split()] for _ in range(n)]

    # Проверка матрицы на сумму.
    flag = 'YES'
    res = n * (n ** 2 + 1) / 2
    for i in range(n):
        total_v, total_main_diag, total_secondary_diag = 0, 0, 0

        for j in range(n):
            total_v += matrix[j][i]
            if i == j:
                total_main_diag += matrix[i][j]
            if j == n - i - 1:
                total_secondary_diag += matrix[i][j]

        if matrix[i] != res and total_v != res and total_main_diag != res and total_secondary_diag != res:
            flag = 'NO'
            break

    # Проверка на последовательность чисел.
    if flag == 'YES':
        tmp = [_ for _ in range(1, (n ** 2) + 1)]
        matrix = [matrix[i][j] for j in range(n) for i in range(n)]
        for t in tmp:
            if t not in matrix:
                flag = 'NO'
                break
        tmp.clear()
    print(flag)


def chess_board():
    size = input().split()
    n, m = int(size[0]), int(size[1])
    matrix = [['.' for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i % 2 == 1 and j % 2 == 0:
                matrix[i][j] = '*'
            elif i % 2 == 0 and j % 2 == 1:
                matrix[i][j] = '*'

    for row in matrix:
        print(*row)


"""
for i in range(n):
    for j in range(1 - i % 2, m, 2):
        board[i][j] = '*'
"""


def side_diagonal():
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        matrix[i][n - 1 - i] = 1
        for j in range(n):
            if i + j + 1 > n:
                matrix[i][j] = 2

    for row in matrix:
        print(*row)


def completion_1():
    # Input matrix.
    n, m = [int(i) for i in input().split()]

    # Data matrix.
    total = 1
    matrix = []
    for i in range(n):
        elem = [_ for _ in range(total, m + total + 1)]
        total = max(elem)
        matrix.append(elem)

    # Print matrix.
    for row in range(n):
        for col in range(m):
            print(str(matrix[row][col]).ljust(3), end='')
        print()


def completion_2():
    # Input.
    n, m = [int(i) for i in input().split()]
    matrix = [[0] * m for _ in range(n)]

    # Data.
    for i in range(n):
        for j in range(m):
            matrix[i][j] = j * n + i + 1

    # Print.
    for row in range(n):
        for col in range(m):
            print(str(matrix[row][col]).ljust(3), end='')
        print()


def completion_3():
    # Input.
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    # Data.
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i - 1:
                matrix[i][j] = 1

    # Print.
    for i in range(n):
        for j in range(n):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


def completion_4():
    # Input.
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    # Data.
    for i in range(n):
        for j in range(n):
            if (i <= j and i <= n - 1 - j <= n) or (i >= j and i >= n - 1 - j):
                matrix[i][j] = 1

    # Print.
    for i in range(n):
        for j in range(n):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


def completion_5():
    # Input.
    n, m = [int(i) for i in input().split()]

    # Data.
    matrix = []
    for i in range(n):
        for j in range(m):
            elem = [_ for _ in range(1, m + 1)]
            elem = elem[j:] + elem[:j]
            matrix.append(elem)
    """
    for i in range(n):
        for j in range(m):
            matrix[i][j] = (i + j) % m + 1
    """

    # Print.
    for row in range(n):
        for col in range(m):
            print(str(matrix[row][col]).ljust(3), end='')
        print()


def filling_snake():
    # Input.
    n, m = [int(i) for i in input().split()]
    # matrix = [[0] * m for _ in range(n)]

    # Data.
    matrix = []
    largest = 1
    for i in range(n):
        elem = [_ for _ in range(largest, m + largest)]
        largest = max(elem) + 1

        if i % 2 == 0:
            matrix.append(elem)
        else:
            matrix.append(elem[::-1])
    """
    for i in range(n):
        for j in range(m):
            matrix[i][j] = i * m + j + 1
        if i % 2:
            matrix[i].reverse()
    """

    # Print.
    for row in range(n):
        for col in range(m):
            print(str(matrix[row][col]).ljust(3), end='')
        print()


def filling_diagonals():
    # Input.
    n, m = [int(i) for i in input().split()]
    matrix = [[0] * m for _ in range(n)]

    # Data.
    total = 0
    for q in range(n + m - 1):
        for i in range(n):
            for j in range(m):
                if i + j == q:
                    total += 1
                    matrix[i][j] = total

    # Print.
    for i in range(n):
        for j in range(m):
            print(str(matrix[i][j]).ljust(3), end='')
        print()


def filling_spiral():
    # Input.
    n, m = [int(i) for i in input().split()]
    matrix = [[0] * m for _ in range(n)]

    # Data.
    i = 1
    x = 0
    y = -1
    row = 0  # 1 0 -1 0
    col = 1  # 0 -1 0 1
    while i <= n * m:
        if 0 <= x + row < n and y + col < m and matrix[x + row][y + col] == 0:
            x += row
            y += col
            matrix[x][y] = i
            i += 1
        else:
            if col == 1:  # Down.
                col, row = 0, 1
            elif row == 1:  # Left.
                row, col = 0, -1
            elif col == -1:  # Up.
                col, row = 0, -1
            elif row == -1:  # Right.
                row, col = 0, 1

    # Print.
    [print(*[str(matrix[i][j]).ljust(3) for j in range(m)]) for i in range(n)]


def test():
    n = 3
    m = 2
    arr1 = [[i] * m for i in range(1, n + 1)]

    arr2 = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr2[i][j] = 1 * j + m * i + 1

    a = np.array(arr1)
    b = np.array(arr2)

    # matrix = a + b
    # matrix = b * 3
    # matrix = np.dot(a, b)
    # matrix = a @ b
    # arr1 = [[1, -1, 0],
    #         [3, -4, 2]]
    #
    # matrix = np.dot(arr1, arr2)

    arr3 = np.matrix([[1, 0], [4, 1]])
    res = arr3 ** 25
    for row in res:
        print(*row)


def matrix_addition():
    # Input.
    n, m = [int(i) for i in input().split()]
    arr1 = [[int(num) for num in input().split()] for _ in range(n)]
    input()
    arr2 = [[int(num) for num in input().split()] for _ in range(n)]

    # Data.
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = arr1[i][j] + arr2[i][j]

    # Numpy.
    matrix = np.array(arr1) + np.array(arr2)

    # Print.
    for row in matrix:
        print(*row)


def matrix_multiplication():
    # Insert.
    n, m = [int(num) for num in input().split()]
    matrix_a = [[int(num) for num in input().split()] for _ in range(n)]
    input()

    m, k = [int(num) for num in input().split()]
    matrix_b = [[int(num) for num in input().split()] for _ in range(m)]

    matrix_c = [[0] * m for i in range(n)]

    # Data.
    # Numpy
    # matrix_c = np.dot(matrix_a, matrix_b)
    # -----
    for i in range(n):
        for j in range(m):
            for p in range(m):
                matrix_c[i][j] += (matrix_a[i][p] * matrix_b[p][j])

    # Print.
    for row in matrix_c:
        print(*row)


def exponentiation_matrix():
    # Input.
    n = int(input())
    arr = [[int(num) for num in input().split()] for _ in range(n)]
    m = int(input())

    # Data.
    res = np.matrix(arr) ** m

    # Print.
    for row in np.array(res):
        print(*row)


###################################
# Экзамен.
###################################

# n, m = [int(i) for i in input().split()]


def matrix_input():
    matrix = [[0] * m for _ in range(n)]
    return matrix


def matrix_print(matrix):
    # if out:
    for row in matrix:
        print(*row)
    # else:
    #     for i in range(n):
    #         for j in range(m):
    #             print(str(matrix[i][j]).ljust(3), end='')
    #         print()

def every_element():
    text = input().split()
    n = int(input())
    matrix = [[0] for _ in range(n)]

    total = 0
    for c in text:
        if total < n:
            if matrix[total][0] == 0:
                matrix[total][0] = c
            else:
                matrix[total].append(c)
        else:
            total = 0
            matrix[total].append(c)

        total += 1

    print(matrix)

def maximum_area_2():
    # Input.
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]

    # Data.
    largest = matrix[0][0]
    for i in range(n):
        for j in range(n):
            if i + j + 1 >= n and largest < matrix[i][j]:
                largest = matrix[i][j]

    print(largest)

def matrix_transposition():
    # Input.
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print()

def snowflake():
    # Input.
    n = int(input())
    matrix = [['.'] * n for i in range(n)]

    # Data.
    for i in range(n):
        matrix[i][i] = '*'
        matrix[i][n - i - 1] = '*'
        for j in range(n):
            matrix[int(n / 2)][j] = '*'
            matrix[i][int(n / 2)] = '*'

    # Print.
    for row in matrix:
        print(*row)

def symmetric_matrix():
    # Input.
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]

    # Data.
    flag = True
    for i in range(n):
        for j in range(n):
            if i + j + 1 < n or i + j + 1 > n:
                if matrix[i][j] != matrix[n-j-1][n-i-1]:
                    flag = False
                    break
    # Print.
    if flag:
        print('YES')
    else:
        print('NO')

def latin_square():
    # Input.
    n = int(input())
    matrix = [[int(num) for num in input().split()] for _ in range(n)]
    tmp = [_ for _ in range(1, n+1)]

    # Data.
    arr = [[0] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][0] == 0:
                arr[i][0] = matrix[j][i]
            else:
                arr[i].append(matrix[j][i])

    flag = True
    for num in tmp:
        for i in range(n):
            if num not in matrix[i] or num not in arr[i]:
                flag = False
                break

    # Print.
    print('YES' if flag else 'NO')

def queen_moves():
    # Координаты коня.
    cordinat = input()
    horizont = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    h = ''
    if cordinat[0] in horizont:
        h = horizont.index(cordinat[0])
    v = int(cordinat[1])

    # Инициализируем доску.
    n = 8
    matrix = [['.'] * n for _ in range(n)]

    # Ход коня.
    for x in range(1, n + 1):
        for y in range(n):
            if (x == v or y == h) or (x - y == v - h or x + y == h + v):
                matrix[-x][y] = '*'
    matrix[-v][h] = 'Q'

    # Вывод доски.
    for row in matrix:
        print(*row)


def diagonals_parallel_main():
    # Input.
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    # Data.
    for i in range(n):
        for j in range(n):
            if i > j:
                res = i - j
            else:
                res = j - i
            matrix[i][j] = res
    """
    arr = [[abs(i - j) for j in range(n)] for i in range(n)]
    """

    # Print.
    for row in matrix:
        print(*row)


def main():
    diagonals_parallel_main()
    # queen_moves()
    # latin_square()
    # symmetric_matrix()
    # snowflake()
    # matrix_transposition()
    # maximum_area_2()
    # every_element()
    # exponentiation_matrix()
    # matrix_multiplication()
    # matrix_addition()
    # test()
    # filling_spiral()
    # filling_diagonals()
    # filling_snake()
    # completion_5()
    # completion_4()
    # completion_3()
    # completion_2()
    # completion_1()
    # side_diagonal()
    # chess_board()
    # magic_square()
    # knight_move()
    # matrix_rotation()
    # mirroring()
    # exchange_diagonals()
    # symmetric_matrix()
    # column_swapping()
    # maximum_table()
    # multiplication_table()
    # sums_quarters()
    # max_area()
    # more_average()
    # matrix_trace()
    # output_matrix_2()
    # test()


if __name__ == '__main__':
    main()
