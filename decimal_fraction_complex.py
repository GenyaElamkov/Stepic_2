from decimal import Decimal
from fractions import Fraction
from math import factorial, gcd


###################
# Модуль Decimal.
###################

def decimal_1() -> None:
    """Выводит сумму наибольшего и наименьшего Decimal числа."""
    s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 ' \
        '6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 ' \
        '5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
    s = [Decimal(i) for i in s.split()]
    print(sum((max(s), min(s))))


def decimal_2() -> None:
    """Вывел на первой строке сумму всех чисел, а на второй строке 5 самых больших чисел в порядке убывания,
    разделенных символом пробела."""
    s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 ' \
        '8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 ' \
        '5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'

    s = [Decimal(i) for i in s.split()]
    print(sum(s))
    print(*sorted(s, reverse=True)[:5])


def decimal_3() -> None:
    """Выводит сумму наибольшей и наименьшей цифры Decimal числа."""
    """
    Sample Input 1:
   
     12.1244354689
    Sample Output 1:
    10
    """
    num = Decimal(input())
    nums = num.as_tuple().digits
    if len(nums) == abs(num.as_tuple().exponent):
        nums = nums + (0,)
    print(sum((max(nums), min(nums))))


def mathematical_expression() -> None:
    """Вычисляет значение выражения."""
    d = Decimal(input())

    result = d.exp() + d.ln() + d.log10() + d.sqrt()
    print(result)


#####################
# Модуль Fraction.
#####################

def fraction_1() -> None:
    """Каждого десятичного числа вывел его представление в виде обыкновенной дроби в формате."""
    numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
               '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
               '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
               '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']

    for n in numbers:
        print(f'{n} = {Fraction(n)}')


def fraction_2() -> None:
    """Выводит сумму наибольшего и наименьшего числа в виде обыкновенной дроби."""

    s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 ' \
        '6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 ' \
        '5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'

    s = [Fraction(n) for n in s.split()]
    print(sum([max(s), min(s)]))


def shorten_fraction() -> None:
    """Сокращает дробь и выводит ее"""
    n, d = [int(input()) for _ in range(2)]

    print(Fraction(n, d))


def operations_fractions() -> None:
    """Вычисляет и выводит их сумму, разность, произведение и частное."""
    n1, n2 = [input() for _ in range(2)]
    print(f'{n1} + {n2} = {Fraction(n1) + Fraction(n2)}')
    print(f'{n1} - {n2} = {Fraction(n1) - Fraction(n2)}')
    print(f'{n1} * {n2} = {Fraction(n1) * Fraction(n2)}')
    print(f'{n1} / {n2} = {Fraction(n1) / Fraction(n2)}')

    """
    operators = {'+': F.__add__, '-': F.__sub__, '*': F.__mul__, '/': F.__truediv__}
    a, b = [input() for _ in '..']
    ops = [*map(F, (a, b))]
    for op in operators:
        print(f'{a} {op} {b} = {operators[op](*ops)}')
    """


def sum_fractions_1() -> None:
    """Вычисляет и выводит рациональное число, равное значению выражения."""

    n = int(input())

    res = sum([Fraction(1, i) ** 2 for i in range(1, n + 1)])
    print(res)


def sum_fractions_2() -> None:
    """Вычисляет и выводит рациональное число, равное значению выражения."""
    n = int(input())
    res = sum([Fraction(1, factorial(i)) for i in range(1, n + 1)])
    print(res)


def young_mathematician() -> None:
    """Находит наибольшую правильную несократимую дробь с суммой числителя и знаменателя равной n."""
    n = int(input())
    tmp = 0
    for i in range(1, n+1):
        for j in range(n, 0, -1):
            if gcd(i, j) == 1 and i < j and sum([i, j]) == n:
                if tmp < Fraction(i, j):
                    tmp = Fraction(i, j)
    print(tmp)


def ordered_fractions() -> None:
    """Выводит в порядке возрастания все несократимые дроби, заключённые между 0 и 1,
    знаменатель которых не превосходит n."""

    n = int(input())
    arr_fraction = []
    for i in range(1, n+1):
        for j in range(n, 0, -1):
            if gcd(i, j) == 1 and i < j:
                arr_fraction.append(Fraction(i, j))

    print(*sorted(arr_fraction), sep='\n')

    """
    numbers = set()

    for i in range(2, int(input()) + 1):
        for j in range(1, i):
            numbers.add(Fraction(j, i))
    """


def main():
    # ordered_fractions()
    young_mathematician()
    # sum_fractions_2()
    # sum_fractions_1()
    # operations_fractions()
    # shorten_fraction()
    # fraction_2()
    # fraction_1()
    # mathematical_expression()
    # decimal_3()
    # decimal_2()
    # decimal_1()


if __name__ == '__main__':
    main()
