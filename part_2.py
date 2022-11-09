def more_revious():
    num = list(input().split())
    counter = sum([True for i in range(1, len(num)) if int(num[i]) > int(num[i - 1])])
    print(counter)

    # counter = 0
    # for i in range(1, len(num)):
    #     if int(num[i]) > int(num[i - 1]):
    #         counter += 1
    #         print(num[i])


def back_foraward():
    num = list(input().split())
    for i in range(1, len(num), 2):
        num[i - 1], num[i] = num[i], num[i - 1]
    print(*num)


def shift_development():
    num = input().split()
    num.insert(0, num.pop(-1))
    print(*num)


def various_elements():
    num = input().split()
    print(len(set(num)))


def product_numbers():
    colect = [int(input()) for _ in range(int(input()))]
    lagest = int(input())
    flag = 'НЕТ'
    for i in range(len(colect)):
        for j in range(i + 1, len(colect)):
            if lagest == colect[i] * colect[j]:
                flag = 'ДА'
                break
    print(flag)


def rock_scissors_paper():
    # timur = input().lower()
    # ruslan = input().lower()
    # arr = ['ножницы', 'бумага', 'камень']
    # if timur == arr[0] and ruslan == arr[1]:
    #     resoult = 'Тимур'
    # elif timur == arr[1] and ruslan == arr[2]:
    #     resoult = 'Тимур'
    # elif timur == arr[2] and ruslan == arr[0]:
    #     resoult = 'Тимур'
    # elif timur == ruslan:
    #     resoult = 'ничья'
    # else:
    #     resoult = 'Руслан'
    #
    # print(resoult)

    x, y = input(), input()
    var = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']
    ans = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
    print(ans[var.index(x) - var.index(y)])

    # if ((var.index(x) - var.index(y)) > 3) / 2:
    #     print(ans.index(2))
    # elif ((var.index(x) - var.index(y)) < -3) / 2:
    #     print(ans.index(-2))
    # else:


def orel():
    text = input()
    counter = 0
    largest = 0
    for c in text:
        if c == 'Р':
            counter += 1
        else:
            counter = 0

        if counter > largest:
            largest = counter

    print(largest)
    s = input().split('О')
    print(len(max(s)))

    print(len(max(input().split('О'), key=len)))


def silicon_valley():
    text = [input() for _ in range(int(input()))]
    name = ['a', 'n', 't', 'o', 'n']

    for i in range(len(text)):
        start = 0
        for j in range(len(name) - 1):
            start = text[i].find(name[j], start)
            end = text[i].find(name[j + 1], start)
            if start < end:
                start = end
            else:
                break
        else:
            print(i + 1, end=' ')

        # for i in range(int(input())):
        #     s, virus, x = input(), 'anton', 0
        #     for sym in s:
        #         if sym == virus[x]:
        #             x += 1
        #         if x == 5:
        #             print(i + 1, end=' ')
        #             break


def roskomnadzor():
    # text = f"{input()} запретил букву"
    # arr_chr = sorted(set([ord(c) for c in text.replace(' ', '')]))
    # arr_chr = sorted(set(text))
    # for num in arr_chr:
    #     print(f'{" ".join(text.split())} {chr(num)}')
    #     text = text.replace(chr(num), '')

    text = f"{input()} запретил букву"
    arr_chr = sorted(set(text.replace(' ', '')))
    for sym in arr_chr:
        print(f'{" ".join(text.split())} {sym}')
        text = text.replace(sym, '')

# word = input() + ' запретил букву'





def main():
    roskomnadzor()
    # silicon_valley()
    # orel()
    # rock_scissors_paper()
    # product_numbers()
    # various_elements()
    # shift_development()
    # back_foraward()
    # more_revious()


if __name__ == '__main__':
    main()
