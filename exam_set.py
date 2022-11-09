""""Экзамен множество"""

def homework():
    """
    n - школьники
    m - дом задание съела собака
    k - откл свет
    p - постикла оба несчастьяя
    :return:
    """
    n, m, k, p = [int(input()) for _ in range(4)]

    res = n - p - (m - p) - (k - p)
    print(res)


def sunrise():
    num = input().split()
    # num2 = num1.copy()
    res = len(num) - len(set(num))

    print(res)


def cities():
    arr = [input() for _ in range(int(input()))]
    new_city = input()
    print('REPEAT' if new_city in arr else 'OK')


def books_read():
    m = int(input())
    n = int(input())

    name_m = [input() for _ in range(m)]
    name_n = [input() for _ in range(n)]
    name_m = set(name_m)
    for word in name_n:
        if word in name_m:
            print('YES')
        else:
            print('NO')


def strange_hobby():
    list_1 = set(input().split())
    list_2 = set(input().split())
    res = list_1.intersection(list_2)
    res = sorted([int(i) for i in res], reverse=True)
    if len(res) != 0:
        print(*res)
    else:
        print('BAD DAY')


def beegeek_1():
    num_1 = set(input().split())
    num_2 = set(input().split())
    # res = True
    # for n in num_1:
    #     if n not in num_2:
    #         res = False
    #         break
    #
    print('YES' if num_1 == num_2 else 'NO')
    print()


def beegeek_2():
    m = int(input())
    n = int(input())

    name_m = set([input() for _ in range(m)])
    name_n = set([input() for _ in range(n)])
    name_m.difference_update(name_n)
    print(len(name_m))


def beegeek_3():
    m = int(input())
    n = int(input())

    name_m = set([input() for _ in range(m)])
    name_n = set([input() for _ in range(n)])
    res = name_m.symmetric_difference(name_n)
    print('NO' if len(res) == 0 else len(res))


def beegeek_4():
    m = set(input().split())
    n = set(input().split())

    print(*sorted(m.union(n)))


def beegeek_5():
    m = int(input())
    n = int(input())

    name = [input() for _ in range(m + n)]
    name_1 = set(name)
    res_len = len(name) - len(name_1)
    if len(name) / 2 == len(name_1):
        res = 'NO'
    else:
        res = len(name) - res_len * 2
    print(res)


def beegeek_6():
    m = int(input())
    arr = [{input() for _ in range(int(input()))} for _ in range(m)]

    res = arr[0]
    for i in range(len(arr)-1):
        res = res.intersection(arr[i+1])

    print(*sorted(res), sep='\n')


def main():
    beegeek_6()
    # beegeek_5()
    # beegeek_4()
    # beegeek_3()
    # beegeek_2()
    # beegeek_1()
    # strange_hobby()
    # books_read()
    # cities()
    # sunrise()
    # homework()


if __name__ == '__main__':
    main()
