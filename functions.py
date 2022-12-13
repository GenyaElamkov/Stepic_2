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

    arr = [arg for arg in args if type(arg) == int or type(arg) == float]
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
        if type(product) == str and product:
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


def main():
    print(info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher'))
    # print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
    # print(greet('Timur'))
    # print(mean(-1, 2, 3, 10, ('5')))
    # print(sq_sum(2))
    # print(count_args([], (''), 'a', 12, False))
    # print(matrix(3), sep='\n')


if __name__ == '__main__':
    main()
