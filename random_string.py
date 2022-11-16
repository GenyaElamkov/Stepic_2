import random
from random import sample, shuffle, choice, uniform
from string import digits, ascii_uppercase, ascii_letters, ascii_lowercase


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
    """Программа, которая считывает одно слово и выводит с помощью модуля random его случайную анаграму."""

    word = list(input())
    random.shuffle(word)
    print(*word, sep='')


def bingo():
    """Программа, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго."""

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
    который будет вместе решать задачи по программированию.
    """
    arr_fio = [input() for _ in range(int(input()))]
    temp = arr_fio.copy()
    random.shuffle(temp)
    d = {}
    for i in range(len(temp) - 1):
        if i < len(temp):
            d.setdefault(temp[i], temp[i + 1])
    else:
        d.setdefault(temp[-1], temp[0])

    for key in arr_fio:
        print(f'{key} - {d[key]}')


def password_generator_1():
    """
    Генератор n паролей длиной m символов, состоящих из строчных и прописных английских букв и цифр,
    кроме тех, которые легко перепутать между собой.
    «l» (L маленькое);
    «I» (i большое);
    «1» (цифра);
    «o» и «O» (большая и маленькая буквы);
    «0» (цифра).
    """

    def generate_password(length):
        # chars = digits + ascii_letters
        # symbols = 'Il1o0O'
        # for c in symbols:
        #     chars = chars.replace(c, '')

        chars = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
        return ''.join(sample(chars, length))

    def generate_passwords(count, length):
        return [generate_password(length) for _ in range(count)]

    n, m = [int(input()) for _ in range(2)]
    print(*generate_passwords(n, m), sep='\n')


def password_generator_2():
    """
    Генератор паролей.
    Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум
    по одной букве в верхнем и нижнем регистре.
    """

    def generate_password(length):
        letters = [ascii_lowercase, ascii_uppercase, digits]
        letters = [''.join(set(letter) - set('lI1oO0')) for letter in letters]

        chars = []
        while len(chars) < length:
            for letter in letters:
                if len(chars) == length:
                    break
                chars += choice(letter)

        shuffle(chars)
        return ''.join(chars)

    def generate_passwords(count, length):
        return [generate_password(length) for _ in range(count)]

    n, m = [int(input()) for _ in range(2)]
    print(*generate_passwords(n, m), sep='\n')


def area_figure():
    """
    При поомощи метода Монте-Карло вычисляет площадь фигуры,
    задаваемой с помощью системы неравенств.
    """
    n = 10 ** 6
    k = 0
    s0 = 16
    for _ in range(n):
        x = uniform(-2, 2)
        y = uniform(-2, 2)

        if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
            k += 1
    print((k / n) * s0)


def pi_area():
    """При помощи метода Монте-Карло определяет приближённое значение числа pi."""

    n = 10 ** 6
    k = 0
    s0 = 4
    for _ in range(n):
        x = uniform(-1, 1)
        y = uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            k += 1
    print((k / n) * s0)


def main():
    pi_area()
    # area_figure()
    # password_generator_2()
    # password_generator_1()
    # secret_friend()
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
