from functools import reduce
from math import sqrt, sin
from operator import *


def matrix(n=1, m=None, value=0):
    """
    Cоздает, заполняет и возвращает матрицу заданного размера. При этом (в
    зависимости от переданных аргументов) она должна вести себя так:

        matrix() — возвращает матрицу 1× 1, в которой единственное число
        равно нулю; matrix(n) — возвращает матрицу n× n, заполненную нулями;
        matrix(n, m) — возвращает матрицу из n строк и m столбцов,
        заполненную нулями; matrix(n, m, value) — возвращает матрицу из n
        строк и m столбцов, в которой каждый элемент равен числу value.
    """
    if not m:
        m = n
    return [[value for _ in range(m)] for _ in range(n)]


def count_args(*args):
    """Принимает произвольное количество аргументов и возвращает количество
    переданных в нее аргументов. """
    return len(args)


def sq_sum(*args):
    """Принимает произвольное количество числовых аргументов и возвращает
    сумму их квадратов. """
    return sum(n ** 2 for n in args)


def mean(*args):
    """
    Принимает произвольное количество аргументов и возвращает среднее
    арифметическое переданных в нее числовых (int или float) аргументов.
    """

    arr = [
        arg for arg in args if isinstance(
            arg, int) or isinstance(
            arg, float)]
    if not arr:
        return 0.0
    return sum(arr) / len(arr)


def greet(name, *args):
    """
    Принимает произвольное количество аргументов строк имен
    (как минимум одно) и возвращает приветствие в соответствии с образцом.
    """
    text = f'Hello, {name}'
    if not args:
        text += '!'
    else:
        text += ' and ' + ' and '.join(args) + '!'
    return text
    # return f'Hello, {" and ".join((name,) + args)}!'


def print_products(*args):
    """
    Принимает произвольное количество аргументов и выводит список продуктов
    (любая непустая строка) по образцу: <номер продукта>) <название
    продукта> (нумерация продуктов начинается с единицы). Если среди
    переданных аргументов нет ни одного продукта, необходимо вывести текст
    Нет продуктов.
    """
    counter = 0
    for product in args:
        if isinstance(product, str) and product:
            counter += 1
            print(f'{counter}) {product}')

    if counter == 0:
        print('Нет продуктов')


def info_kwargs(**kwargs):
    """
    Принимает произвольное количество именованных аргументов и печатает
    именованные аргументы в соответствии с образцом: <имя аргумента>:
    <значение аргумента>, при этом имена аргументов следуют в алфавитном
    порядке (по возрастанию).
    """
    for k, v in sorted(kwargs.items()):
        print(f'{k}: {v}')

    # return {k: v for k, v in sorted(kwargs.items())}


def average(pointer):
    # return sum([pointer[i] for i in range(len(pointer))]) / len(pointer)
    return sum(pointer) / len(pointer)


def get_min_max(numbers):
    """
    Программа, которая с помощью встроенных функций min() и max() выводит те
    кортежи (каждый на отдельной строке), которые имеют минимальное и
    максимальное среднее арифметическое значение элементов.
    """
    print(min(numbers, key=average))
    print(max(numbers, key=average))


def means(pointer):
    return sqrt(pointer[0] ** 2 + pointer[1] ** 2)


def sort_numbers(points):
    """
    Программа, которая сортирует список points координат точек плоскости в
    соответствии с расстоянием от начала координат (точки (0;0)). Программа
    должна вывести отсортированный список.
    """
    print(sorted(points, key=means))


def sum_min_max(points):
    return sum((min(points), max(points)))


def sort_sum_min_max(numbers):
    """
    Программу, которая сортирует и выводит список numbers в соответствии
    с суммой минимального и максимального элемента кортежа.
    """
    print(sorted(numbers, key=sum_min_max))


def compare(n):
    def cmp(points):
        return points[n - 1]

    return cmp


def sort_it_as_you_want():
    """
    Список athletes содержит сведения о спортсменах в виде кортежей: (имя,
    возраст, рост, вес). Напишите программу сортировки списка спортсменов по
    указанному полю:

    1: по имени;
    2: по возрасту;
    3: по росту;
    4: по весу.

    На вход программе подается натуральное число от 11 до 44 – номер поля по
    которому требуется отсортировать список.
    """
    athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39),
                ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
                ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
                ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
    n = int(input())

    [print(*s) for s in sorted(athletes, key=compare(n))]


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


def root(n):
    return n ** 0.5


def module(n):
    return abs(n)


def sine(n):
    return sin(n)


def mathematical_functions():
    """
    Программа, которая принимает число и название функции,
    а выводит результат применения функции к данному числу.
    """
    n = int(input())
    name_func = input()

    commands = {'квадрат': square, 'куб': cube, 'корень': root,
                'модуль': module, 'синус': sine}
    print(commands[name_func](n))

    """
    def pwr(p):
        def numpower(n):
            return n**p
        return numpower

    commands = {"квадрат": pwr(2), "куб": pwr(3), "корень": pwr(0.5), 
    "модуль": abs, "синус": math.sin} """


def sow(num):
    # resoult = 0
    # while num != 0:
    #     tmp = num % 10
    #     num //= 10
    #     resoult += tmp
    # return resoult
    return sum(map(int, num))


def interesting_sorting_1():
    """
    Программа сортировки списка чисел в порядке неубывания суммы их цифр.
    При этом, если два числа имеют одинаковую сумму цифр, следует сохранить
    их взаиморасположение в начальном списке.
    """
    # num_list = [int(num) for num in input().split()]
    print(*sorted(input().split(), key=sow))


def sorting_sum(text):
    # text = [int(n) for n in text]
    return sum(map(int, text))


def interesting_sorting_2():
    """
    Программа сортировки списка чисел в порядке неубывания суммы их цифр.
    При этом, если у двух чисел одинаковая сумма цифр, их следует вывести в
    порядке неубывания.
    """
    text = sorted(input().split(), key=int)
    print(*sorted(text, key=sorting_sum))

    """
    def comparator(n):
        return sum([int(i) for i in str(n)]), n
    
    numbers = [int(i) for i in input().split()]
    
    print(*sorted(numbers, key=comparator))
    """


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


def set_round(item):
    return round(item, 2)


def rounds_2():
    """
    Программу, которая с помощью функции map() округляет все элементы списка
    numbers до 22 десятичных знаков, а затем выводит их, каждый на отдельной
    строке.
    """
    numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013,
               23.22222, 90.09873,
               45.45, 314.1528, 2.71828, 1.41546]
    print(*map(set_round, numbers), sep='\n')


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


def select_num(num):
    return num % 5 == 2 and len(str(num)) == 3


def get_cube(num):
    return num ** 3


def selects_three_digit_numbers():
    """
    Программа, которая с помощью функций filter() и map() отбирает из
    заданного списка numbers трёхзначные числа, дающие при делении на 5
    остаток 2, и выводит их кубы, каждый в отдельной строке.
    """
    numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434,
               696, 1016, 1084, 424, 1189, 475, 95,
               1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488,
               668, 944, 207, 266, 1309, 1027, 257,
               1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560,
               338, 232, 182, 1438, 1127, 928, 1309,
               98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166,
               904, 349, 831, 1207, 1496, 370, 725, 926,
               175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138,
               142, 433, 456, 1268, 1018, 1274, 387,
               120, 340, 963, 832, 1127]

    print(*map(get_cube, filter(select_num, numbers)), sep='\n')


# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc


def squares(num):
    return num ** 2


def summa(x, y):
    return x + y ** 2


def output_summa():
    """
    Программа для вычисления и вывода суммы квадратов элементов списка numbers.
    """
    numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46,
               1, -8, 84, 16, 51, 90, 56,
               65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76,
               94, 60, 72, 43, 4, -6, -5,
               51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87,
               81, -7, 57, 26, 36, 17, 43,
               80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95,
               78, 27, 82, 1, 64, 94, 31, 29,
               -8, 98, 24, 61, 7, 73]

    print(sum(map(squares, numbers)))
    print(reduce(summa, numbers, 0))


def get_two_digit_numbers(num):
    return len(str(abs(num))) == 2 and num % 7 == 0


def output_summa_square():
    """
    Программа для вычисления и вывода суммы квадратов двузначных чисел,
    которые делятся на 7 без остатка.
    """
    numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280,
               214, 156, 227, 228, 51, -4, 202, 58, 99,
               270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266,
               180, 6, 279, 200, 208, 231, 178, 201,
               260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258,
               196, -8, 43, 2, 128, 143, 43, 297, 229, 60,
               254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268,
               -9, 23, 71, 135, 7, -161, 65, 135, 29,
               148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184,
               -7, 228, 129, 274, 73, 197, 272, 54, 278,
               26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41,
               269, 94, 279, 129, 39, 92, -63, 263, 219,
               57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229,
               205, 123, -105]

    print(sum(map(squares, filter(get_two_digit_numbers, numbers))))


def func_apply(func, items):
    """
     Функция func_apply(), принимающую на вход функцию и список значений и возвращающую список,
     в котором каждое значение будет результатом применения переданной функции к переданному списку.
    """
    return list(map(func, items))


def add3(x):
    return x + 3


"""
Требовалось написать программу, которая:

преобразует список floats в список чисел, возведенных в квадрат и округленных с 
точностью до одного десятичного знака;
фильтрует список words  и оставляет только палиндромы длиной более 4 символов;
находит произведение чисел из списка numbers.
Программист торопился и написал программу неправильно. Доработайте его программу.
"""
floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45,
          9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic',
         'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num ** 2, 1), floats))
filter_result = list(
    filter(lambda name: name == name[::-1] and len(name) > 4, words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

"""
Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() 
выводит в алфавитном порядке список primary городов с населением более 10000000 человек, в формате:

Cities: Beijing, Buenos Aires, ...
"""
data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

filter_primary = list(filter(lambda word: 'primary' in word, data))
filter_million = list(
    map(lambda n: n[0], filter(lambda n: n[1] > 10_000_000, filter_primary)))
sort_filter_million = sorted(filter_million)
print_res = reduce(lambda x, y: x + ' ' + y + ',', sort_filter_million,
                   'Cities:')[:-1]
# s = list(filter(lambda x:x[1] > 10_000_000 and x[2] == 'primary', data))

#######################
#  Модуль № 8
######################

"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и возвращает
 значение True, если он делится без остатка на 1919 или на 1313 и False в противном случае.
"""
func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
# print(func(247))


"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает 
значение True, если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен) 
и False в противном случае.
"""
func_1 = lambda word: word.lower().startswith('a') and word[
    -1].lower().endswith('a')
# print(func_1('abcdA'))


"""Напишите функцию is_non_negative_num, используя синтаксис анонимных 
функций, которая принимает строковый аргумент и возвращает значение True, 
если переданный аргумент является неотрицательным числом (целым или 
вещественным) и False в противном случае. """
is_non_negative_num = lambda n: n.replace('.', '', 1).isnumeric()
# print(is_non_negative_num('12300'))


"""
Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает
значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.
"""
is_num = lambda n: False if '-' in n[1:] else n.replace('-', '', 1).replace(
    '.', '', 1).isnumeric()
# is_num = lambda n: is_non_negative_num(n[1:]) if q[0] == '-' else is_non_negative_num(n)
# print(is_num('-11'))


"""
Напишите программу, которая с помощью встроенных функций filter() и sorted() выводит слова из списка words, 
имеющие длину ровно 6 символов. Слова следует вывести в алфавитном порядке на одной строке, разделив символом пробела.
"""
words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse',
         'abuse', 'bid', 'wednesday', 'able',
         'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides',
         'access', 'friday', 'bestow',
         'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard',
         'about', 'accelerate', 'abort', 'thursday',
         'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate',
         'abide', 'bicycle', 'beside', 'accept',
         'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
print_words = sorted(filter(lambda x: len(x) == 6, words))
# print(*print_words)


"""
Напишите программу, которая с помощью встроенных функций map() и filter() удаляет из списка numbers все нечетные 
элементы, большие 47, а все четные элементы нацело делит на два (целочисленное деление – //). Полученные числа 
следует вывести на одной строке, разделив символом пробела и сохранив исходный порядок.
"""
numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34,
           100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
           93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72,
           32, 41, 59, 35, 64, 49, 78, 83, 27,
           57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26,
           6, 4, 23, 52, 39, 63, 74, 15, 66, 29,
           88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46,
           33]

numbers_filter = map(lambda n: n // 2 if n % 2 == 0 else n,
                     filter(lambda n: n < 47 or n % 2 == 0, numbers))
# print(*numbers_filter)

"""
Список data содержит информацию о численности населения некоторых штатов США. Напишите программу 
сортировки по убыванию списка data на основании последнего символа в названии штата. Затем распечатайте
элементы этого списка, каждый на новой строке в формате:

<название штата>: <численность населения>

Vermont: 626299
Massachusetts: 7029917
...
"""

data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'),
        (626299, 'Vermont'),
        (1805832, 'West Virginia'), (39865590, 'California'),
        (11799448, 'Ohio'), (10711908, 'Georgia'),
        (10077331, 'Michigan'), (10439388, 'Virginia'),
        (7705281, 'Washington'), (7151502, 'Arizona'),
        (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

sort_data = sorted(data, key=lambda x: x[1][-1], reverse=True)
# print(*[f'{v}: {k}' for k, v in sort_data], sep='\n')


"""
Список data содержит слова на русском языке. Напишите программу его сортировки по возрастанию длины слов,
а затем в лексикографическом порядке. Отсортированные слова следует вывести на одной строке, разделив символом пробела.
"""
data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз',
        'работа', 'слово', 'место', 'лицо', 'друг',
        'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай',
        'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

sorting_data = sorted(sorted(data), key=len)
# print(*sorting_data)
# print(*sorted(data, key=lambda x: (len(x), x)))


"""
Список mixed_list содержит целочисленные и строковые значения. Напишите программу, которая с помощью встроенной 
функции max() находит и выводит наибольшее числовое значение в указанном списке.

Примечание 1. Для решения задачи используйте анонимную функцию и необязательный аргумент key  функции max().

Примечание 2. Обратите внимание, что сравнивать числа и строки нельзя.
"""

mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate',
              'accessory', 'absorb', 1384878, 'sunday',
              'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970,
              1772933, 1564063, 'abduct', 901271,
              2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry',
              433507, 'bias', 'bestow', 1875665, 'besides',
              'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal',
              2286106, 242192, 701049, 2866491, 'benevolent',
              'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280,
              686008, 'beyond', 2415643, 'aboard', 'bet',
              859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543,
              1619426, 2263113, 1618068, 'berth',
              'abolish', 'beware', 2618492, 1555062, 'access', 'absent',
              'abundant', 2950603, 'betray', 'beverage',
              'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday',
              810387, 'friday', 2576799, 2213552,
              1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326,
              1499197, 2241159, 605320, 2347441]

max_mixed_list = max(mixed_list, key=lambda x: x if isinstance(x, int) else 0)
# print(max_mixed_list)


"""
Список mixed_list содержит целочисленные и строковые значения. Напишите программу его сортировки по неубыванию
значений элементов, при этом числа должны следовать до строк.  Элементы отсортированного списка выведите на одной 
строке, разделив символом пробела.
"""

mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides',
              'berry', 15, 65, 'abate', 'thursday', 76,
              70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid',
              'sunday', 'saturday', 87, 'bigot', 41, 'abort',
              13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75,
              13, 40, 67, 12, 'abuse', 78, 10, 80,
              'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51,
              95, 'abduct', 37, 98, 99, 14, 'abandon',
              'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound',
              12, 95, 'wednesday', 'abundant', 'abrupt',
              'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46,
              'betray', 47, 'able', 11]

sort_mixed_list = sorted(mixed_list, key=lambda x: (isinstance(x, str), x))


# print(*sort_mixed_list)


def opposite_color():
    """
    Противоположный цвет
    В цветовой схеме RGB цвета задаются с помощью трех компонентов:

    R — интенсивность красной составляющей цвета;
    G — интенсивность зеленой составляющей цвета;
    B — интенсивность синей составляющей цвета.
    Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B). Считается, что такие цвета хорошо гармонируют друг
    с другом.

    Напишите программу, которая по трем компонентам заданного цвета, находит компоненты противоположного цвета.
    """

    color = map(lambda x: 255 - int(x), input().split())
    print(*color)


def evaluate(coefficients, x):
    """
    Программа, которая вычисляет значение указанного многочлена при заданном значении x.
    """
    multiply = map(lambda b, a: b * x ** a, coefficients,
                   range(len(coefficients) - 1, -1, -1))
    res_sum = reduce(lambda a, b: a + b, multiply, 0)
    print(res_sum)

    # evaluate = lambda coefficients, x: reduce(lambda s, a: s * x + a, coefficients, 0)
    # print(evaluate([*map(int, input().split())], int(input())))


def ignore_command(command):
    """
    Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,
    и возвращает значение True, если в команде содержится подстрока из списка ignore и False – если нет.
    """
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update',
              'exec', 'del', 'truncate']
    return any(map(lambda x: x in command, ignore))


"""
Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о стране.
Для каждой страны информацию выводить на отдельной строке. 
<capital> is the capital of <country>, population equal <population> people.
"""
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511,
              1_380_004_385]


# for cap, count, pops in zip(capitals, countries, population):
#     print(f"{cap} is the capital of {count}, population equal {pops} people.")


def set_ball():
    """
    На вход программе подаются три строки текста с вещественными числами, значениями абсцисс (x), ординат (y) и
    аппликат (z) точек трехмерного пространства. Напишите программу для проверки расположения всех точек с
    введенными координатами внутри либо на поверхности шара с центром в начале координат и радиусом R = 2. Формат
    входных данных На вход программе подаются три строки текста с вещественными числами, разделенными символом
    пробела – абсциссы, ординаты и аппликаты точек в трехмерной системе координат.

    Формат выходных данных Программа должна вывести True если все точки с
    введенными координатами находятся внутри или на границе шара и False,
    если вне.
    """

    # abscissas = map(float, input().split())
    # ordinates = map(float, input().split())
    # applicates = map(float, input().split())
    abscissas, ordinates, applicates = (map(float, input().split()) for _ in
                                        range(3))
    r = 2  # Радиус шара.
    print(all([x ** 2 + y ** 2 + z ** 2 <= r ** 2 for x, y, z in
               zip(abscissas, ordinates, applicates)]))


def correct_ip_address():
    """
    IP-адрес – уникальный числовой идентификатор устройства в компьютерной
    сети, работающей по протоколу TCP/IP.

    В 4-й версии IP-адрес представляет собой 32-битное число. Адрес
    записывается в виде четырёх десятичных чисел (октетов) со значением от 0
    до 255 (включительно), разделённых точками, например, 192.168.1.2.

    Напишите программу с использованием встроенной функции all() для проверки корректности IP-адреса: все ли октеты в
    IP-адресе – числа со значением от 00 до 255.
    """
    adsress = input().split('.')
    test = all(map(lambda n: n.isdigit() and 0 <= int(n) <= 255, adsress))
    print(test)


def interesting_numbers():
    """
    На вход программе подаются два натуральных числа a и b. Напишите программу с использованием встроенной функции
    all() для обнаружения всех целых чисел в диапазоне [a;b], которые делятся на каждую содержащуюся в них
    цифру без остатка.
    """
    a, b = [int(input()) for _ in range(2)]
    generation_num = list(range(a, b + 1))

    for num in generation_num:
        res = map(lambda x: x != 0 and num % x == 0, map(int, str(num)))

        if all(res):
            print(num, end=' ')


def good_password():
    """
    Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру,
    заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный
    пароль.
    """
    password = input()
    p_len = len(password) >= 7
    p_isupper = any(map(lambda x: x.isupper(), password))
    p_islower = any(map(lambda x: x.islower(), password))
    p_isdigit = any(map(lambda x: x.isdigit(), password))

    print('YES' if all([p_len, p_isupper, p_islower, p_isdigit]) else 'NO')

    """
    s = input()
    print('YES' if all((any(i.isupper() for i in s), 
                    any(i.islower() for i in s), 
                    any(i.isdigit() for i in s), 
                    len(s) >= 7)) else 'NO')
    """


def honors_students():
    """
    Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил
    убедиться, что в каждом классе есть хотя бы один отличник – ученик с оценкой 5 по контрольной работе. Напишите
    программу с использованием встроенных функций all(), any() для помощи Тимуру в проверке.

    Формат входных данных На вход программе подается натуральное число n – количество классов. Затем для каждого класса
    вводится блок информации вида:

    натуральное число k – количество учеников в классе;
    далее вводится k строк вида: фамилия оценка.
    Формат выходных данных
    Программа должна вывести YES, если в каждом классе есть хотя бы один отличник, и NO в противном случае.
    """

    res = []
    for _ in range(int(input())):
        students = [input().endswith('5') for _ in range(int(input()))]
        res.append(any(students))

    print('YES' if all(res) else 'NO')


#######################
#
#  Экзамен.
#
######################

def test():
    """
    test func
    """
    return lambda x: x * 2


#
# arr = list(range(10))
# res = filter(lambda x: x % 2 == 0 and x != 0, arr)
# print(any(map(lambda x: x % 2 == 0 and x != 0, arr)))
#
# lam = lambda x: x + 100
# print(lam(10))
# print(lam.__defaults__)


def a():
    def b(x):
        return x ** 2

    return b


def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев',
                    number=17):
    """
    To: <mail>
    Приветствую, <name>!
    Вам назначен экзамен, который пройдет <date>, в <time>.
    По адресу: <place>.
    Экзамен будет проводить <teacher> в кабинете <number>.
    Желаем удачи на экзамене!
    """
    mails = f"To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, " \
            f"который пройдет {date}, в {time}.\nПо адресу: {place}.\n" \
            f"Экзамен будет проводить {teacher} в кабинете {number}.\n" \
            f"Желаем удачи на экзамене! "
    return mails


def pretty_print(data, side='-', delimiter='|'):
    word = delimiter + ' '
    for d in data:
        word += str(d) + ' ' + delimiter + ' '
    # word = word[:-1]
    t = len(word) - 3
    print(f" {side * t} \n{word[:-1]}\n {side * t} ")


def concat(*args, sep=' '):
    # return sep.join([str(_) for _ in args])
    # return sep.join(args)
    # print(*args, sep=sep)
    return sep.join(map(str, args))


def product_of_odds(data):
    # result = 1
    # for i in data:
    #     if i % 2 == 1:
    #         result *= i
    # return result

    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)


words = 'the world is mine take a look what you have started'.split()

# print(*map(lambda x: f'"{x}"', words))

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565,
# 5665, 10, 1000, 908, 909, 232, 45654, 786] print(*filter(lambda x: x != x[
# ::-1], map(str, numbers)))

numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1),
           (17, 0, 1), (0, 1), (3,), (39, 12),
           (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)


# print(sorted_numbers)

def mul7(x):
    return x * 7


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z


def call(func, *args):
    return func(*args)


# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))


def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def compose(f, g):
    def func(x):
        return f(g(x))

    return func


# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))


def arithmetic_operation(oper):
    kw = {"+": add,
          "-": sub,
          "*": mul,
          "/": truediv}

    def fun(x, y):
        return sum(map(kw[oper], [x], [y]))

    return fun


"""
def arithmetic_operation(operation):
    oper = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    return oper[operation]
"""

add = arithmetic_operation('+')
div = arithmetic_operation('/')


# print(add(10, 20))
# print(div(20, 5))

def test():
    text = 'cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats ' \
           'CatAlo'.split()
    # text = input().split()
    print(text)
    res = sorted(text, key=lambda x: x.lower())
    print(*res)


def test_2():
    def t(word):
        return sum(map(lambda x: ord(x.upper()) - ord('A'), word))

    text = [input() for _ in range(int(input()))]
    res = sorted(sorted(text), key=t)
    print(*res, sep='\n')


def test_3():
    # multiply = map(lambda b, a: b * x ** a, coefficients, range(len(
    # coefficients) - 1, -1, -1)) res_sum = reduce(lambda a, b: a + b,
    # multiply, 0) print(res_sum)
    def s(ip):
        res = list(map(int, ip.split('.')))
        tmp = list(map(lambda x, a: x * 256 ** a, res, range(4 - 1, -1, -1)))
        return sum(tmp)

    arr = [input() for _ in range(int(input()))]

    print(*sorted(arr, key=s), sep='\n')


def main():
    test_3()
    # test_2() test() print(product_of_odds([1,2,3])) print(concat('hello',
    # 'python', 'and', 'stepik')) print(concat('hello', 'python', 'and',
    # 'stepik', sep='*')) print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
    # pretty_print([1, 2, 10, 23, 123, 3000]) print(generate_letter(
    # 'lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус
    # 2')) t = a() print(t(3)) a = test() honors_students() good_password()
    # interesting_numbers() correct_ip_address() set_ball() print(
    # ignore_command('get ip')) print(ignore_command('select all')) print(
    # ignore_command('delete')) print(ignore_command('trancate'))

    # coefficients = [int(num) for num in input().split()]
    # x = int(input())
    # evaluate(coefficients, x)
    # opposite_color()
    # print(map_result)
    # print(filter_result)
    # print(reduce_result)
    # print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
    # output_summa_square()
    # output_summa()
    # selects_three_digit_numbers()
    # rounds_2()
    # interesting_sorting_2()
    # interesting_sorting_1()
    # mathematical_functions()
    # sort_it_as_you_want()

    # numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12,
    # 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50,
    # 40, 50), (34, 78, 65), (-5, 90, -1)] sort_sum_min_max(numbers)

    # points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0),
    # (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)] sort_numbers(points)

    # numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,),
    # (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40,
    # 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
    # (90, 1, -45, -21)] get_min_max(numbers)

    # print( info_kwargs( first_name='Timur', last_name='Guev', age=28,
    # job='teacher')) print_products('Бананы', [1, 2], ('Stepik',),
    # 'Яблоки', '', 'Макароны', 5, True) print(greet('Timur')) print(mean(
    # -1, 2, 3, 10, ('5'))) print(sq_sum(2)) print(count_args([], (''), 'a',
    # 12, False)) print(matrix(3), sep='\n')


if __name__ == '__main__':
    main()
