from random import choice


def file_1():
    """
    На вход программе подается строка с именем текстового файла. Напишите программу, которая выводит на экран его
    предпоследнюю строку.
    """
    file = open(input(), 'r', encoding='utf-8')
    print(file.readlines())
    file.close()


def file_2():
    """
    Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную
    строку из этого файла.
    """
    t = 'lines.txt'
    file = open(t, 'r', encoding='utf-8')
    print(choice(file.readlines()))
    file.close()


def file_3():
    """
    Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число. Напишите программу,
    выводящую на экран сумму этих чисел.
    """
    file = open('numbers.txt', 'r', encoding='utf-8')
    print(sum(map(int, file.readlines())))

    file.close()


def file_4():
    """
    Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами
    пробела и конца строки. Напишите программу, выводящую на экран сумму этих чисел.
    """
    file = open('nums.txt', 'r', encoding='utf-8')
    content = [int(x) for x in map(str.strip, file.readlines()) if x]
    print(sum(content))
    file.close()
    # print(sum(map(int, file.read().split())))


def file_5():
    """
    Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью
    символа табуляции (\t) разделена на три колонки:

    наименование товара;
    количество товара (целое число);
    цена (в рублях) товара за 11 шт (целое число).
    Напишите программу, выводящую на экран общую стоимость заказа.
    """
    file = open('prices.txt', 'r', encoding='utf-8')
    sum = 0
    for line in file:
        price = int(line.split('\t')[-1].strip())
        counter = int(line.split('\t')[-2])
        res = counter * price
        sum += res
    print(sum)

    file.close()
    # lines = map(str.split, file)
    # print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))

def main():
    file_5()
    # file_4()
    # file_3()
    # file_2()
    # file_1()
    # file = open('test.txt', 'r', encoding='utf-8')
    # cont = file.readlines()
    # cont = [line.strip() for line in cont]
    # cont = list(map(str.strip, cont))
    # print(cont)
    # print(list(file)) # Тоже самое что и file.readlines()
    # print(file.encoding)
    # print(file)
    # file.close()
    # print(file.closed)


if __name__ == '__main__':
    main()
