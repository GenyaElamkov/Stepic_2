# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = sum([sum(i) for i in list1])
# counter = sum([len(i) for i in list1])
#
# resoult = total / counter
# print(resoult)
#
# # Method 1
# m, n = 5, 2
# arr = []
# for _ in range(m):
#     arr.append([0] * n)
# # print(arr)
#
# # Method 2
# arr = [0] * m
# for i in range(m):
#     arr[i] = [0] * n
# arr[0][0] = 17
# # print(arr)
#
# # Method 3
# arr = [[0] * n for i in range(m)]
# arr[0][0] = 17
# # print(arr)
#
# srr = [[0] * n] * m
# srr[0][0] = 17
# # print(srr)
#
# n = 4
# arr = []

# for _ in range(n):
#     elem = [int(i) for i in input().split()]
#     arr.append(elem)
# print(arr)


# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#
# total = 0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         total += arr[i][j]
# print(total)
#
# res = sum([sum(i) for i in arr])
# print(res)
#
# list1 = [[1, 2, 3], [4, 5, 6]]
# list2 = list1
# list1[0].append(7)
# print(list2)

# arr = [[i]*i for i in range(1, int(input())+1)]
# --------------------------
def queste_1():
    n = int(input())
    # arr = []
    # for row in range(n):
    #     elem = [_ for _ in range(1, n+1)]
    #     arr.append(elem)
    arr = [[_ for _ in range(1, n + 1)] for _ in range(n)]
    print(*arr, sep='\n')
    print('-' * 50)

    result = []

    for _ in range(n):
        result.append(list(range(1, n + 1)))

    print(*result, sep='\n')


def quested_2(n):
    res = [list(range(1, i + 1)) for i in range(1, n + 1)]
    print(*res, sep='\n')


from math import factorial, comb


def pascal(n):
    # arr = [int(factorial(n) / (factorial(n - i) * factorial(i))) for i in range(n + 1)]
    arr = [int(comb(n, i)) for i in range(n + 1)]
    return arr


def pascal1(n):
    res = []
    for j in range(n):
        elem = [int(factorial(j) / (factorial(j - i) * factorial(i))) for i in range(j + 1)]
        res.append(elem)

    # for i in range(len(res)):
    #     for j in range(len(res[i])):
    #         print(res[i][j], end=' ')
    #     print()
    #
    # -------------------ФУНКЦИЯ-------------------
    n = int(input())
    pasc = []
    for i in range(0, n):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != i and j != 0:
                row[j] = pasc[i - 1][j - 1] + pasc[i - 1][j]
        pasc.append(row)


def packing_duplicates():
    # text = input().split()
    # char_list = []
    # tmp = []
    # for char in text:
    #     if not bool(tmp):
    #         tmp.append(char)
    #     else:
    #         if tmp[-1] == char:
    #             tmp.append(char)
    #         else:
    #             char_list.append(tmp)
    #             tmp = [char]
    #
    # if bool(tmp):
    #     char_list.append(tmp)
    # print(char_list)

    # arr = []
    # tmp = []
    # for c in text.split():
    #     if not tmp:
    #         tmp.append(c)
    #     else:
    #         if tmp[-1] == c:
    #             tmp.append(c)
    #         else:
    #             arr.append(tmp)
    #             tmp = [c]
    # if tmp:
    #     arr.append(tmp)
    # return arr

    res = []

    for el in input().split():
        if res and el in res[-1]:
            res[-1].append(el)
        else:
            res.append([el])

    print(res)


# def chunked(text, num):
#     counter = 0
#     tmp = []
#     arr = []
#     for c in text.split():
#         if counter == num:
#             arr.append(tmp)
#             tmp = [c]
#             counter = 0
#         else:
#             tmp.append(c)
#
#         counter += 1
#
#     if tmp:
#         arr.append(tmp)
#
#     return arr


def chunked_2(text, num):
    arr = []
    for c in text.split():
        if arr and len(arr[-1]) != num:
            arr[-1].append(c)
        else:
            arr.append([c])
    return arr


def sublists_list():
    # text = input().split()
    text = 's t e p i k r o c k s'.split()
    arr = []
    for i in range(len(text)):
        for j in range(len(text)):
            tmp = text[j:i + j + 1]
            if len(tmp) == i + 1:
                arr.append(tmp)
            else:
                break

    print([[]] + arr)


def main():
    sublists_list()
    # text = input()
    # num = int(input())
    # print(chunked_2(text, num))
    # print(chunked(text, num))
    # text = input()
    # print(packing_duplicates(text))
    # n = int(input())
    # print(pascal(n))
    # pascal1(n)


if __name__ == '__main__':
    main()
