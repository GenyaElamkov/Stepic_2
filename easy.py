from math import log, log2


def line_cost():
    word = input()
    lens = len(word) * 60
    print(f'{lens // 100} р. {lens % 100} коп.')


def body_mass_index():
    weight = float(input())
    height = float(input())
    res = weight / (height ** 2)
    if 18.5 <= res <= 25:
        resoult = 'Оптимальная масса'
    elif res < 18.5:
        resoult = 'Недостаточная масса'
    else:
        resoult = 'Избыточная масса'

    print(resoult)


def easy():
    a, b = int(input()), int(input())
    print(a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) ** 0.5, sep='\n')


def zodiac():
    zod = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']
    year = int(input())
    index = year % 12 - 2000 % 12
    print(zod[index])


def test():
    num = input()
    # if len(num) < 6:
    #     resoult = num[::-1]
    # else:
    #     resoult = num[0] + num[:-6:-1]
    # print(int(resoult))

    resoult = num[::-1] if len(num) < 6 else num[0] + num[:-6:-1]
    print(int(resoult))

    print(int(s[:-5] + s[-5:][::-1]))


def standard_american_convention():
    num = list(input())
    counter = -3
    for i in range(len(num) // 3):
        num.insert(counter, ',')
        counter -= 4
    print(''.join(num).strip(','))



def josephus():
    n = int(input())
    k = int(input())

    res = 0
    for i in range(1, n + 1):
        res = (res + k) % i
    print(res + 1)



def joseph(n, k):
    if n == 1:
        return 1
    return (joseph(n-1, k) + k - 1) % n + 1


def coordinate():
    counter1, counter2, counter3, counter4 = 0, 0, 0, 0
    for i in range(int(input())):
        coord = input().split()
        x, y = int(coord[0]), int(coord[1])
        if x > 0 and y > 0:
            counter1 += 1
        elif x < 0 and y > 0:
            counter2 += 1
        elif x < 0 and y < 0:
            counter3 += 1
        elif x > 0 and y < 0:
            counter4 += 1

    print(f'Первая четверть: {counter1}')
    print(f'Вторая четверть: {counter2}')
    print(f'Третья четверть: {counter3}')
    print(f'Четвертая четверть: {counter4}')

    n = int(input())
    count = [0, 0, 0, 0]
    names = ['Первая четверть:', 'Вторая четверть:',
             'Третья четверть:', 'Четвертая четверть:']

    for _ in range(n):
        x, y = [int(num) for num in input().split()]
        if x > 0 and y > 0:
            count[0] += 1
        elif x < 0 and y > 0:
            count[1] += 1
        elif x < 0 and y < 0:
            count[2] += 1
        elif x > 0 and y < 0:
            count[3] += 1

    for i in range(4):
        print(names[i], count[i])




def main():
    coordinate()
    # josephus()
    # print(joseph(6, 3))
    # standard_american_convention()
    # test()
    # zodiac()
    # line_cost()
    # body_mass_index()
    # easy()


if __name__ == '__main__':
    main()
