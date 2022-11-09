import random
from string import ascii_uppercase


def test_1():
    """моделирует броски монеты"""

    for i in range(int(input())):
        print('Решка' if random.randint(0, 1) else 'Орел')


def test_2():
    """моделирует броски игрального кубика c 6 гранями"""

    for _ in range(int(input())):
        print(random.randint(1, 6))


def test_3():
    """генерирует случайный пароль"""

    length = int(input())  # длина пароля.
    password = []
    for _ in range(length):
        c1 = random.randint(65, 90)
        c2 = random.randint(97, 122)
        password.append(chr(random.choice([c1, c2])))

    print(*password, sep='')


def test_4():
    """генерирует 7 различных случайных чисел для лотерейного билета"""

    result = sorted([random.randint(1, 49) for _ in range(7)])
    print(*result, sep=' ')


def generate_ip():
    """генерирует и возвращает случайный корректный IP адрес"""

    arr = random.sample(range(0, 256), 4)
    return '.'.join(list(map(str, arr)))


def generate_index():
    """генерирует и возвращает случайный корректный почтовый индекс Латверии"""

    letter = ''.join(random.sample(ascii_uppercase, 4))
    num = random.sample(range(0, 100), 2)
    return f'{letter[:2]}{num[0]}_{num[1]}{letter[2:]}'


def random_matrix():
    """перемешивает случайным образом содержимое матрицы"""
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    # for m in matrix:
    #     random.shuffle(m)
    [random.shuffle(m) for m in matrix]
    print(matrix)

def main():
    random_matrix()
    # print(generate_index())
    # print(generate_ip())
    # test_4()
    # test_3()
    # test_2()
    # test_1()


if __name__ == '__main__':
    main()
