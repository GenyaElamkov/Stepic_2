from random import choice, sample


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
    with open("files/data.txt", "r", encoding="utf-8") as f:
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
        with open("files/data.csv", "r", encoding="utf-8") as f:
            header = f.readline().strip().split(',')
            arr = []
            for cont in f:
                cont = cont.strip().split(',')
                arr.append(dict(zip(header, cont)))

        return arr

    print(read_csv())


def input_string():
    """
    Напишите программу, которая считывает строку текста и записывает её в
    текстовый файл output.txt.
    """
    line = input()
    with open("files/output.txt", "w", encoding="utf-8") as f:
        f.write(line)

    # Или так
    # print(input(), file=open('output.txt', 'w'))


def random_numbers():
    """
    Напишите программу, записывающую в текстовый файл random.txt 2525
    случайных чисел в диапазоне от 111111 до 777777 (включительно), каждое с
    новой строки.
    """
    with open("random.txt", "w", encoding="utf-8") as f:
        arr_num = sample(range(111, 778), 25)
        print(*arr_num, sep='\n', file=f)


def line_numbering():
    """
    Вам доступен текстовый файл input.txt, состоящий из нескольких строк.
    Напишите программу для записи содержимого этого файла в файл output.txt
    в виде нумерованного списка, где перед каждой строкой стоит ее номер,
    символ ) и пробел. Нумерация строк должна начинаться с 1.
    """

    with open("input.txt", "r", encoding="utf-8") as f, \
            open("files/output.txt", "w", encoding="utf-8") as out:
        for i, val in enumerate(f.readlines(), 1):
            print(f"{i}) {val.strip()}", file=out)


def gift_for_the_new_year():
    """
    Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест
    на строках вида: фамилия оценка (фамилия и оценка разделены пробелом).
    Оценка - целое число от 0 до 100 включительно.

    Напишите программу для добавления 5 баллов к каждому результату теста и
    вывода фамилий и новых результатов тестов в файл new_scores.txt.
    """
    with open("class_scores.txt", "r", encoding="utf-8") as f_1, \
            open("new_scores.txt", "w", encoding="utf-8") as f_2:
        for line in f_1:
            name, score = line.split()
            print(f"{name} {min(100, int(score) + 5)}", file=f_2)


def riddle_jacques_fresco():
    """
    Однажды Жака Фреско спросили:

    "Если ты такой умный, почему не богатый?"

    Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал
    загадку спрашивающему:

    "Были разноцветные козлы. Сколько?"

    "Сколько чего?"

    "Сколько из них составляет более 7% от общего количества козлов?"

    Вам доступен текстовый файл goats.txt в первой строке которого написано
    слово COLOURS, далее идет список всех возможных цветов козлов. Затем идет
    строка со словом GOATS, и далее непосредственно перечисление козлов разных
    цветов. Перечень козлов включает только строки из первого списка.

    Напишите программу создания файла answer.txt и вывода в него списка козлов,
    которые удовлетворяют условию загадки от Жака Фреско.
    """

    with open("goats.txt", "r", encoding="utf-8") as f_1, \
            open("answer.txt", "w", encoding="utf-8") as f_2:

        colours = []
        for line in f_1:
            if line.strip() == 'GOATS':
                break
            colours.append(line.strip())

        colours.remove('COLOURS')

        goats = [line.strip() for line in f_1]

        for word in colours:
            res = len(goats) / 100 * goats.count(word)
            if res > 7:
                print(f"{word}", file=f_2)
    #     s = txt.readlines()
    #     s = s[s.index("GOATS\n") + 1:]
    #     for i in sorted(set(s)):
    #         if s.count(i) / len(s) > 0.07:
    #             file.write(i)


def file_concatenation():
    """
    На вход программе подается натуральное число nn и nn строк с названиями
    файлов. Напишите программу, которая создает файл output.txt и выводит в
    него содержимое всех файлов с указанными именами, не меняя их порядка.
    """
    # names_files = [input() for _ in range(int(input()))]
    names_files = ['test_1.txt', 'test_2.txt']
    for name in names_files:
        with open(name, "r", encoding="utf-8") as f_1, \
                open("files/output.txt", "a", encoding="utf-8") as f_2:
            print(f_1.read(), end='', file=f_2)

    # with open('output.txt', 'w') as out:
    #     for i in range(int(input())):
    #         with open(input()) as f:
    #             out.write(f.read())


def log_file():
    """
    Вам доступен текстовый файл logfile.txt с информацией о времени входа
    пользователя в систему и выхода из нее. Каждая строка файла содержит три
    значения, разделенные запятыми и символом пробела: имя пользователя,
    время входа, время выхода, где время указано в 24-часовом формате.

    Напишите программу, которая создает файл output.txt и выводит в него имена
    всех пользователей (не меняя порядка следования), которые были в сети не
    менее часа.
    """

    def minutes(text):
        hour, minute = [int(num) for num in text.split(":")]
        return hour * 60 + minute

    with open("files/logfile.txt", "r", encoding="utf-8") as log, \
            open("files/output.txt", "w", encoding="utf-8") as out:
        for line in log:
            line = line.strip().split(',')
            times = line[-2:]
            name = line[0]
            start, stop = [minutes(time) for time in times]
            if stop - start >= 60:
                print(name, file=out)

    # def get_diff_mins(time2, time1):
    #     t2 = list(map(int, time2.split(':')))
    #     t1 = list(map(int, time1.split(':')))
    #     return (t2[0] * 60 + t2[1]) - (t1[0] * 60 + t1[1])
    #
    # with open('logfile.txt', encoding='utf-8') as inputf,
    # open('output.txt', 'w') as outputf: for fn in inputf: name, time1,
    # time2 = fn.strip().split(', ') if get_diff_mins(time2, time1) >= 60:
    # print(name, file=outputf)


########################
#
# Экзамен.
#
########################

def test_1():
    with open(input(), "r", encoding="utf-8") as f:
        print(len(f.readlines()))


def test_2():
    with open("files/ledger.txt", "r", encoding="utf-8") as f:
        context = f.read().strip().replace("$", "").split()
        summa = sum(map(int, context))
        print(f"${summa}")


def test_3():
    with open("files/grades.txt", "r", encoding="utf-8") as f:
        # for line in f:
        #     line = line.split()
        #     t = all(map(lambda x: int(x) >= 65, line[1:]))
        print(
            sum([all(map(lambda x: int(x) >= 65, line.split()[1:])) for line in
                 f]))
        # print(t)


def test_4():
    with open("files/words.txt", "r", encoding="utf-8") as f:
        context = f.read().split()
        largest = len(max(context, key=len))
        res = filter(lambda x: len(x) == largest, context)
        print(*res, sep='\n')


def test_5():
    with open(input(), "r", encoding="utf-8") as f:
        context = f.readlines()[-10:]
        # context = f.readlines()
        print(*context, sep='')


def test_6():
    with open("files/forbidden_words.txt", "r", encoding="utf-8") as forb, \
            open(input(), "r", encoding="utf-8") as f:
        worning = forb.read().split()
        context = f.read()
        context_lower = context.lower()

        for world in worning:
            context_lower = context_lower.replace(world, len(world) * "*")

        res = ''
        for k, c in enumerate(context_lower):
            if c != '*':
                res += context[k]
            else:
                res += "*"

        print(res)


def test_7():
    """
    Перерешать.
    """
    with open("files/cyrillic.txt", "r", encoding="utf-8") as f_1, \
            open("files/transliteration.txt", "w", encoding="utf-8") as f_2:
        d = {
            'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c',
            'в': 'v', 'м': 'm', 'ч': 'ch',
            'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh',
            'е': 'e', 'п': 'p', 'ъ': '*',
            'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'",
            'з': 'z', 'т': 't', 'э': 'je',
            'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
            'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L',
            'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
            'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh',
            'Е': 'E', 'П': 'P', 'Ъ': '*',
            'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'",
            'З': 'Z', 'Т': 'T', 'Э': 'Je',
            'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya'
        }

        # content = f_1.read()
        # for k, v in d.items():
        #     content = content.replace(k, v)
        # print(content, file=f_2)

        for s in f_1.read():
            res = d.get(s.lower(), s)
            f_2.write(res if s.islower() else res.capitalize())


def test_8():
    with open(input(), "r", encoding="utf-8") as f:
        content = f.readlines()
        flag = True
        for i, line in enumerate(content):
            if "def" in line and "#" not in content[i - 1]:
                flag = False
                print(line[line.find(" "): line.find("(")])

        if flag:
            print("Best Programming Team")


def main():
    # test_8()
    test_7()
    # test_6()
    # test_5()
    # test_4()
    # test_3()
    # test_2()
    # test_1()
    # log_file()
    # file_concatenation()
    # riddle_jacques_fresco()
    # gift_for_the_new_year()
    # line_numbering()
    # random_numbers()
    # input_string()
    # csv_file()
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
