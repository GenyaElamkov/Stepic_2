from random import choice


def file_1():
    """
    На вход программе подается строка с именем текстового файла. Напишите
    программу, которая выводит на экран его предпоследнюю строку.
    """
    file = open(input(), 'r', encoding='utf-8')
    print(file.readlines())
    file.close()


def file_2():
    """
    Вам доступен текстовый файл lines.txt из нескольких строк. Напишите
    программу, которая выводит на экран случайную строку из этого файла.
    """
    t = 'lines.txt'
    file = open(t, 'r', encoding='utf-8')
    print(choice(file.readlines()))
    file.close()


def file_3():
    """
    Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них
    записано целое число. Напишите программу, выводящую на экран сумму этих
    чисел.
    """
    file = open('numbers.txt', 'r', encoding='utf-8')
    print(sum(map(int, file.readlines())))

    file.close()


def file_4():
    """
    Вам доступен текстовый файл nums.txt. В файле записано два целых числа,
    они могут быть разделены символами пробела и конца строки. Напишите
    программу, выводящую на экран сумму этих чисел.
    """
    file = open('nums.txt', 'r', encoding='utf-8')
    content = [int(x) for x in map(str.strip, file.readlines()) if x]
    print(sum(content))
    file.close()
    # print(sum(map(int, file.read().split())))


def file_5():
    """
    Вам доступен текстовый файл prices.txt с информацией о заказе из
    интернет магазина. В нем каждая строка с помощью символа табуляции (\t)
    разделена на три колонки:

    наименование товара;
    количество товара (целое число);
    цена (в рублях) товара за 1 шт (целое число).
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


def file_6():
    """
    Вам доступен текстовый файл text.txt с одной строкой текста. Напишите
    программу, которая выводит на экран эту строку в обратном порядке.
    """
    with open('text.txt', 'r', encoding='utf-8') as f:
        content = f.readline()[::-1]
        print(content)


def file_7():
    """
    Вам доступен текстовый файл data.txt, в котором записаны строки текста.
    Напишите программу, выводящую все строки данного файла в обратном
    порядке: сначала последнюю, затем предпоследнюю и т.д.
    """
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f.readlines()[::-1]:
            print(line.strip())


def file_8():
    """
    Вам доступен текстовый файл lines.txt, в котором записаны строки текста.
    Напишите программу, которая выводит все строки наибольшей длины из
    файла, не меняя их порядок.
    """
    with open("lines.txt", "r", encoding="utf-8") as f:
        content = f.readlines()
        largest = len(max(content, key=len))
        # for line in content:
        #     if len(line) == largest:
        #         print(line.strip())
        # print()
        print(*list(
            map(str.strip, filter(lambda x: len(x) == largest, content))),
              sep='\n')


def main():
    file_8()
    # file_7()
    # file_6()
    # file_5()
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
