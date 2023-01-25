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


def file_9():
    """
    Вам доступен текстовый файл numbers.txt, каждая строка которого может
    содержать одно или несколько целых чисел, разделенных одним или
    несколькими пробелами.

    Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит
    эту сумму на экран (для каждой строки выводится сумма чисел в этой строке).
    """

    with open("numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(sum(map(int, line.split())))


def file_10():
    """
    Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые
    неотрицательные числа и все, что угодно. Числом назовем
    последовательность одной и более цифр, идущих подряд (число всегда
    неотрицательно).

    Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.
    """
    with open("nums.txt", "r", encoding="utf-8") as f:
        summa = 0
        for line in f:
            for c in line:
                if not c.isnumeric():
                    line = line.replace(c, ' ')
            summa += sum(map(int, line.split()))
    print(summa)

    # with open('numbers.txt', encoding='utf-8') as file:
    # row = ''.join(c if c.isdigit() else ' ' for c in file.read())
    # print(sum(map(int, row.split())))


def file_11():
    """
    Вам доступен текстовый файл file.txt, набранный латиницей. Напишите
    программу, которая выводит количество букв латинского алфавита, слов и
    строк. Выведите три найденных числа в формате, приведенном в примере.
    """

    with open("files/file.txt", "r", encoding="utf-8") as f:
        context = f.readlines()
        # Кол-во строчек.
        counter_line = len(context)
        # Кол-во слов.
        counter_word = sum([len(word.split()) for word in context])
        # Кол-во букв.
        counter_char = sum([c.isalpha() for line in context for c in line])

    print(f"Input file contains:\n"
          f"{counter_char} letters\n"
          f"{counter_word} words\n"
          f"{counter_line} lines")

    # txt = f.read()
    # print('Input file contains:')
    # print(sum(map(str.isalpha, txt)), 'letters')
    # print(len(txt.split()), 'words')
    # print(txt.count('\n') + 1, 'lines'


def random_name_and_surname():
    """
    Вам доступны два текстовых файла first_names.txt и last_names.txt,
    один с именами, другой с фамилиями.

    Напишите программу, которая c помощью модуля random создает 33 случайные
    пары имя + фамилия, а затем выводит их, каждую на отдельной строке.
    """
    with open("first_names.txt", "r", encoding="utf-8") as first_names, \
            open("last_names.txt", "r", encoding="utf-8") as last_names:
        for _ in range(3):
            first = choice(first_names.read().split())
            last = choice(last_names.read().split())
            first_names.seek(0), last_names.seek(0)

            print(f"{first} {last}")
    # z, x = f.readlines(), l.readlines()
    # for i in range(3):
    #     print(random.choice(z).strip(), random.choice(x).strip(), sep=' ')


def unusual_countries():
    """
    Вам доступен текстовый файл population.txt с названиями стран и
    численностью их населения, разделенными символом табуляции '\t'.

    Напишите программу выводящую все страны, название которых начинается с
    буквы 'G', численность населения которых больше чем 500 000 человек,
    не меняя их порядок.
    """

    with open("population.txt", "r", encoding="utf-8") as f:
        for line in f:
            content = line.split()
            if content[0].startswith('G') and int(content[-1]) > 500_000:
                print(*content[:-1])
    # for line in f:
    #     n, p = line.split('\t')
    #     if n.startswith('G') and int(p) > 500000:
    #         print(n)


def csv_file():
    """
    Вам доступен CSV-файл data.csv, содержащий информацию в csv формате.
    Напишите функцию read_csv для чтения данных из этого файла. Она должна
    возвращать список словарей, интерпретируя первую строку как имена
    ключей, а каждую последующую строку как значения этих ключей.
    """
    def read_csv():
        with open("data.csv", "r", encoding="utf-8") as f:

            header = f.readline().strip().split(',')
            arr = []
            for cont in f:
                cont = cont.strip().split(',')
                arr.append(dict(zip(header, cont)))

        return arr

    print(read_csv())



def main():
    csv_file()
    # unusual_countries()
    # random_name_and_surname()
    # file_11()
    # file_10()
    # file_9()
    # file_8()
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
