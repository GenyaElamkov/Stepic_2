import random
from string import ascii_uppercase


def test_1():
    """Моделирует броски монеты"""

    for i in range(int(input())):
        print('Решка' if random.randint(0, 1) else 'Орел')


def test_2():
    """Моделирует броски игрального кубика c 6 гранями"""

    for _ in range(int(input())):
        print(random.randint(1, 6))


def test_3():
    """Генерирует случайный пароль"""

    length = int(input())  # длина пароля.
    password = []
    for _ in range(length):
        c1 = random.randint(65, 90)
        c2 = random.randint(97, 122)
        password.append(chr(random.choice([c1, c2])))

    print(*password, sep='')


def test_4():
    """Генерирует 7 различных случайных чисел для лотерейного билета"""

    result = sorted([random.randint(1, 49) for _ in range(7)])
    print(*result, sep=' ')


def generate_ip():
    """Генерирует и возвращает случайный корректный IP адрес"""

    arr = random.sample(range(0, 256), 4)
    return '.'.join(list(map(str, arr)))


def generate_index():
    """Генерирует и возвращает случайный корректный почтовый индекс Латверии"""

    letter = ''.join(random.sample(ascii_uppercase, 4))
    num = random.sample(range(0, 100), 2)
    return f'{letter[:2]}{num[0]}_{num[1]}{letter[2:]}'


def random_matrix():
    """Перемешивает случайным образом содержимое матрицы"""
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    # for m in matrix:
    #     random.shuffle(m)
    [random.shuffle(m) for m in matrix]
    print(matrix)


def random_lottery_ticket_numbers():
    """
    Cлучайные номера лотерейных билетов.
    - номер не может начинаться с нулей;
    - номер лотерейного билета должен состоять из 7 цифр;
    - все 100 лотерейных билетов должны быть различными.
    """

    arr = [[random.choice(range(1, 9))] + random.sample(range(0, 9), 6) for _ in range(100)]

    for i in arr:
        for j in i:
            print(j, end='')
        print()


def anagram():
    """Программа, которая считывает одно слово и выводит с помощью модуля random его случайную анаграму"""

    word = list(input())
    random.shuffle(word)
    print(*word, sep='')


def bingo():
    """Программа, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго"""
    # matrix = [[random.randint(1, 75) for _ in range(5)] for _ in range(5)]
    # matrix[2][2] = 0
    # for i in matrix:
    #     for j in i:
    #         print(str(j).ljust(3), end='')
    #     print()

    arr = random.sample(list(range(1, 76)), 25)
    random.shuffle(arr)
    arr[12] = 0
    for i, val in enumerate(arr, 1):
        print(str(val).ljust(3), end='')
        if i % 5 == 0:
            print('')


def secret_friend():
    """
    Случайным образом назначает каждому ученику его тайного друга,
    который будет вместе с ним решать задачи по программированию
    """
    arr_fio = [input() for _ in range(int(input()))]
    temp = arr_fio.copy()

    print(arr_fio)

    for i in range()
    # Имя Фамилия и Имя - Фамилия (тайного друга)


def main():
    secret_friend()
    # bingo()
    # anagram()
    # random_lottery_ticket_numbers()
    # random_matrix()
    # print(generate_index())
    # print(generate_ip())
    # test_4()
    # test_3()
    # test_2()
    # test_1()


if __name__ == '__main__':
    main()
