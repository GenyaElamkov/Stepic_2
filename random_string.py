import random


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


def main():
    test_4()
    # test_3()
    # test_2()
    # test_1()


if __name__ == '__main__':
    main()
