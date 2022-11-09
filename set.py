"""Множество"""

def timur_his_team():
    n, m, k, x, y, z = [int(input()) for _ in range(6)]
    count = (n - x) + (k - y) + (m - x - y) + x + y + z
    print(count)


def books_read():
    n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

    nm = n + m - x - 2
    mk = m + k - y - 2
    nk = n + k - z - 2
    n = n - 2 - nm - nk
    m = m - 2 - nm - mk
    k = k - 2 - nk - mk

    # Прочитали только одну книгу.
    read_one_book = n + m + k
    # Прочитали две книги.
    read_two_book = nm + mk + nk
    # Не прочитали ни одной из рекомендованных книг.
    no_read_book = a - (nm + mk + nk + 2 + n + m + k)

    resoult = [read_one_book, read_two_book, no_read_book]
    print(*resoult, sep='\n')


def time_set():
    """Сравниваем множества, списки и кортежи"""
    from time import time
    from sys import getsizeof

    # Просьба не ставить большие числа. В count хранится правая граница range для объектов.
    # В foriner – правая граница for ... in range

    count = 10000000
    foriner = count

    print("В этом алгоритме сравниваются множество, список и кортеж на скорость и время", end="\n\n")
    print("Правая граница интервала —", count)
    my_set = set(range(1, count + 1))
    my_list = list(range(1, count + 1))
    my_tuple = tuple(range(1, count + 1))

    my_set_size = getsizeof(my_set)
    my_list_size = getsizeof(my_list)
    my_tuple_size = getsizeof(my_tuple)

    print()
    print(f"Память {{множес.}} = {my_set_size} байт = {round(my_set_size / 1024, 3)} Кб \
        = {round(my_set_size / 1024 / 1024, 3)} Мб")
    print(f"Память [списка]  = {my_list_size} байт = {round(my_list_size / 1024, 3)} Кб \
        = {round(my_list_size / 1024 / 1024, 3)} Мб")
    print(f"Память (кортежа) = {my_tuple_size} байт = {round(my_tuple_size / 1024, 3)} Кб \
        = {round(my_tuple_size / 1024 / 1024, 3)} Мб")

    print()

    t = time()
    for i in range(foriner):
        if i in my_set:
            pass
    print(f"Время с множеством: {time() - t} секунд")
    my_set.clear()

    t = time()
    for i in range(foriner):
        if i in my_list:
            pass
    print(f"Время с списком:    {time() - t} секунд")
    my_list.clear()

    t = time()
    for i in range(foriner):
        if i in my_tuple:
            pass
    print(f"Время с кортежам:   {time() - t} секунд")


def test():
    # n = '100000'
    # print('YES' if len(n) == len(set(n)) else 'NO ')
    # n1, n2 = input(), input()
    # print('YES' if len(set(n1 + n2)) == 10 else 'NO')
    # print('YES' if set(input()) == set(input()) else 'NO')

    text = input().split()
    res = all([set(text[i]) == set(text[i + 1]) for i in range(len(text) - 1)])
    print('YES' if res else 'NO')


def unique_characters_1():
    n = int(input())
    # for _ in range(n):
    #     line = input().lower()
    #     print(len(set(line)))
    arr = [len(set(input().lower())) for _ in range(n)]
    print(*arr, sep='\n')


def unique_characters_2():
    n = int(input())
    line = ''
    for _ in range(n):
        line += input().lower()

    print(len(set(line)))


# from string import punctuation
def count_sword():
    text = input().lower()
    text = text.translate(text.maketrans('', '', '.,;:-?!')).split()
    print(len(set(text)))


def next_numbers():
    # num = input().split()
    num = '1 1 2 2 5 5 5 5 6 7 8'.split()

    tmp = set()
    for n in num:
        n = int(n)
        if n in tmp:
            print('YES')
        else:
            print('NO')
            tmp.add(n)


def number_matching():
    n1, n2 = [set(input().split()) for _ in range(2)]
    print(len(n1 & n2))


def common_numbers():
    n1, n2 = [input().split() for _ in range(2)]
    n1 = set(int(i) for i in n1)
    n2 = set(int(i) for i in n2)
    print(*sorted(n1 & n2))
    # set1 = set(int(i) for i in input().split())
    # set2 = set(int(i) for i in input().split())


def numbers_first_row():
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    print(*sorted(set1-set2))


def general_figures():
    arr = [input() for _ in range(int(input()))]
    res = set(arr[0])
    for i in range(len(arr)-1):
        res &= set(arr[i+1])

    print(*sorted(res))


def identical_numbers():
    n1, n2 = [input() for _ in range(2)]
    res = set(n1).isdisjoint(set(n2))
    print('NO' if res else 'YES')


def all_numbers():
    n1, n2 = [input() for _ in range(2)]
    res = set(n1).issuperset(set(n2))
    print('YES' if res else 'NO')


def lesson_information():
    n1, n2, n3 = [input().split() for _ in range(3)]
    n1, n2, n3 = [set(n) for n in [n1, n2, n3]]
    res = n1 & n2

    resoult = sorted([int(num) for num in res if num not in n3], reverse=True)
    print(*resoult)

    """
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())

    print(*sorted(set1 & set2 - set3, reverse=True))
    """


def lesson_matematic():
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())

    resoult = (set1 | set2 | set3) - (set1 & set2 & set3)
    print(*sorted(resoult))


def lesson_fisic():
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())

    resoult = set3 - (set1 | set2)

    print(*sorted(resoult, reverse=True))


def lesson_biologe():
    set1 = set(int(i) for i in input().split())
    set2 = set(int(i) for i in input().split())
    set3 = set(int(i) for i in input().split())

    tmp_set = {_ for _ in range(11)}
    resoult = tmp_set - (set3 | set1 | set2)

    print(*sorted(resoult))


def test():
    files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']

    myset = {word.lower() for word in files if word[-3:].lower() == 'png'}
    # result = {c.lower() for c in files if c.lower().endswith('.png')}

    print(*sorted(myset))



def main():
    test()
    # lesson_biologe()
    # lesson_fisic()
    # lesson_matematic()
    # lesson_information()
    # all_numbers()
    # identical_numbers()
    # general_figures()
    # numbers_first_row()
    # common_numbers()
    # number_matching()
    # next_numbers()
    # count_sword()
    # unique_characters_2()
    # unique_characters_1()
    # test()
    # time_set()
    # books_read()
    # timur_his_team()


if __name__ == '__main__':
    main()
