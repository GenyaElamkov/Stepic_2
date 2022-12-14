import math


def main1():
    numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -
               6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
    res = numbers[0]
    for i in range(len(numbers) - 1):
        res *= numbers[i + 1]
    print(res)

    res = math.prod(numbers)
    print(res)


def main2():
    numbers = ((10, 10, 10, 12), (30, 45, 56, 45),
               (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

    print([sum(num) / len(num) for num in numbers])


def main3():
    # a , b , c
    vertex = [int(input()) for _ in range(3)]
    x = - vertex[1] / (2 * vertex[0])
    y = (4 * vertex[0] * vertex[2] - vertex[1] ** 2) / (4 * vertex[0])
    res = tuple([x, y])

    print(res)


def competitive_selection():
    text = [input() for _ in range(int(input()))]

    print(*text, sep='\n')
    print()
    print(*[line for line in text if int(line[-1]) >= 4], sep='\n')


def fibonach():
    n = int(input())
    f1, f2, f3 = 1, 1, 1
    for _ in range(n):
        print(f1, end=' ')
        f1, f2, f3 = f3, f1 + f2 + f3, f2


def main():
    fibonach()
    # competitive_selection()


if __name__ == '__main__':
    main()
