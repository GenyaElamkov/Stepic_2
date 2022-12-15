from math import sqrt


def matrix(n=1, m=None, value=0):
    """
    Cоздает, заполняет и возвращает матрицу заданного размера.
    При этом (в зависимости от переданных аргументов) она должна вести себя так:

        matrix() — возвращает матрицу 1× 1, в которой единственное число равно нулю;
        matrix(n) — возвращает матрицу n× n, заполненную нулями;
        matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями;
        matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой каждый
        элемент равен числу value.
    """
    if not m:
        m = n
    return [[value for _ in range(m)] for _ in range(n)]


def count_args(*args):
    """Принимает произвольное количество аргументов и возвращает количество переданных в нее аргументов."""
    return len(args)


def sq_sum(*args):
    """Принимает произвольное количество числовых аргументов и возвращает сумму их квадратов."""
    return sum(n ** 2 for n in args)


def mean(*args):
    """
    Принимает произвольное количество аргументов и возвращает среднее арифметическое
    переданных в нее числовых (int или float) аргументов.
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
    (любая непустая строка) по образцу: <номер продукта>) <название продукта>
    (нумерация продуктов начинается с единицы). Если среди переданных аргументов нет ни одного продукта,
    необходимо вывести текст Нет продуктов.
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
    Принимает произвольное количество именованных аргументов и печатает именованные
    аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, при этом
    имена аргументов следуют в алфавитном порядке (по возрастанию).
    """
    for k, v in sorted(kwargs.items()):
        print(f'{k}: {v}')

    # return {k: v for k, v in sorted(kwargs.items())}


def average(pointer):
    # return sum([pointer[i] for i in range(len(pointer))]) / len(pointer)
    return sum(pointer) / len(pointer)


def get_min_max(numbers):
    """
    Программа, которая с помощью встроенных функций min() и max() выводит те кортежи (каждый на отдельной строке),
    которые имеют минимальное и максимальное среднее арифметическое значение элементов.
    """
    print(min(numbers, key=average))
    print(max(numbers, key=average))


def means(pointer):
    return sqrt(pointer[0] ** 2 + pointer[1] ** 2)


def sort_numbers(points):
    """
    Программа, которая сортирует список points координат точек плоскости в соответствии с расстоянием от
    начала координат (точки (0;0)). Программа должна вывести отсортированный список.
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
    Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
    Напишите программу сортировки списка спортсменов по указанному полю:

    1: по имени;
    2: по возрасту;
    3: по росту;
    4: по весу.

    На вход программе подается натуральное число от 11 до 44 – номер поля по которому требуется отсортировать список.
    """
    athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
                ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
    n = int(input())

    [print(*s) for s in sorted(athletes, key=compare(n))]


def main():
    sort_it_as_you_want()

    # numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99),
    #            (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
    # sort_sum_min_max(numbers)

    # points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6),
    #           (8, 8)]
    # sort_numbers(points)

    # numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
    #            (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
    #            (90, 1, -45, -21)]
    # get_min_max(numbers)

    # print(
    #     info_kwargs(
    #         first_name='Timur',
    #         last_name='Guev',
    #         age=28,
    #         job='teacher'))
    # print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
    # print(greet('Timur'))
    # print(mean(-1, 2, 3, 10, ('5')))
    # print(sq_sum(2))
    # print(count_args([], (''), 'a', 12, False))
    # print(matrix(3), sep='\n')


if __name__ == '__main__':
    main()
