from pprint import pprint


def test_1():
    users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
             {'name': 'Helga', 'phone': '555-1618'},
             {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
             {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
             {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
             {'name': 'John', 'phone': '233-421-32', 'email': ''},
             {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
             {'name': 'Alina', 'phone': '+7948-799-2434'},
             {'name': 'Robert', 'phone': '420-2011', 'email': ''},
             {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
             {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
             {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
             {'name': 'Roman', 'phone': '+7459-145-8059'},
             {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
             {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
             {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

    names = []
    for user in users:
        if 'email' not in user or user['email'] == '':
            names.append(user['name'])
    print(*sorted(names))

    # print(*sorted([user['name'] for user in users if 'email' not in user or user['email'] == '']))


def string_representation():
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
               'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num = [int(i) for i in input()]
    for i in num:
        for key, val in numbers.items():
            if val == i:
                print(key, end=' ')


def information_training_courses():
    d = {
        "CS101": "3004, Хайнс, 8:00",
        "CS102": "4501, Альварадо, 9:00",
        "CS103": "6755, Рич, 10:00",
        "NT110": "1244, Берк, 11:00",
        "CM241": "1411, Ли, 13:00"
    }
    number_course = input()

    for key, val in d.items():
        if key == number_course:
            print(f'{key}: {val}')

    # print('{}: {}, {}, {}'.format(s, *courses[s]))


def set_messages():
    symbol = {1: '.,?!:', 2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL',
              6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ', 0: ' '}

    text = input()

    resout = ''
    for char in text.upper():
        for key, val in symbol.items():
            resout += str(key) * (val.find(char) + 1)

    print(resout)


def morse_code():
    letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
             '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
             '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    text = input()
    tmp_letter_morse = dict(zip(letters, morse))

    resout = []
    for char in text.upper():
        for key, val in tmp_letter_morse.items():
            if char == key:
                resout.append(val)

    print(' '.join(resout))

    """
    mydict = dict(zip(letters, morse))
    word = input().upper()

    for c in word:
        if c in mydict:
            print(mydict[c], end=' ')
    """


def metod_get():
    info = {'name': 'Bob',
            'age': 25,
            'job': 'Dev'}

    item1 = info.get('salary')
    item2 = info.get('salary', 'Информации о зарплате нет')

    print(item1)
    print(item2)


def test():
    result = dict(zip(list(range(1, 16)), [i ** 2 for i in range(1, 16)]))
    # result = {}
    # for i in range(1, 16):
    #     result.setdefault(i, i**2)
    print(result)
    #
    # result = {i: i ** 2 for i in range(1, 16)}


def test_1():
    dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
    dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

    result = dict1.copy()
    result.update(dict2)
    for key in dict1.keys():
        if key in dict2:
            result[key] += dict1[key]

    """
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    """


def test_text():
    text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

    result = {}

    for char in text:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    print(result)
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    print(result)


def text_text_2():
    s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana ' \
        'orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon ' \
        'strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley ' \
        'banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry ' \
        'gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum ' \
        'banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime ' \
        'grapefruit pomegranate barley '

    arr = s.split()

    result = {}
    for word in arr:
        result[word] = result.get(word, 0) + 1

    result = dict(sorted(result.items()))
    print(max(result, key=result.get))


def test_text_3():
    pets = [('Hatiko', 'Parker', 'Wilson', 50),
            ('Rusty', 'Josh', 'King', 25),
            ('Fido', 'John', 'Smith', 28),
            ('Butch', 'Jake', 'Smirnoff', 18),
            ('Odi', 'Emma', 'Wright', 18),
            ('Balto', 'Josh', 'King', 25),
            ('Barry', 'Josh', 'King', 25),
            ('Snape', 'Hannah', 'Taylor', 40),
            ('Horry', 'Martha', 'Robinson', 73),
            ('Giro', 'Alex', 'Martinez', 65),
            ('Zooma', 'Simon', 'Nevel', 32),
            ('Lassie', 'Josh', 'King', 25),
            ('Chase', 'Martha', 'Robinson', 73),
            ('Ace', 'Martha', 'Williams', 38),
            ('Rocky', 'Simon', 'Nevel', 32)]

    result = {}
    for name in pets:
        result.setdefault(name[1:], []).append(name[0])

    print(result)


def rarest_word():
    from string import punctuation

    text = input()
    text = text.translate(text.maketrans('', '', punctuation)).lower().split()

    get_dictionary = {}
    for word in text:
        get_dictionary[word] = get_dictionary.get(word, 0) + 1

    get_dictionary = dict(sorted(get_dictionary.items()))
    result = min(get_dictionary, key=get_dictionary.get)
    print(result)


def fixing_duplicates():
    '''
    Output
    a b c a_1 a_2 d c_1
    '''

    text = input().split()
    # text = 'a b c a a d c'.split()
    get_dict = {}
    res = []
    for char in text:
        get_dict[char] = get_dict.get(char, -1) + 1

        if get_dict[char] > 0:
            res.append(f'{char}_{get_dict[char]}')
        else:
            res.append(char)
    print(*res)


def programmer_dictionary():
    definition = [input().split(':') for _ in range(int(input()))]
    definition_dict = {}
    for i in definition:
        definition_dict[i[0].lower()] = i[1][1:]

    words = [input().lower() for _ in range(int(input()))]
    for word in words:
        if word not in definition_dict:
            result = 'Не найдено'
        else:
            result = definition_dict[word]

        print(result)
    """
    mydict = {}

    for _ in range(int(input())):
        key, value = input().split(': ')
        mydict[key.lower()] = value

    for _ in range(int(input())):
        print(mydict.get(input().lower(), 'Не найдено'))
    """


def anagrams_1():
    arr = [sorted(input()) for _ in range(2)]
    print('YES' if arr[0] == arr[1] else 'NO')


def no_spaces_special_characters_nums(string: str) -> str:
    return ''.join(c for c in string if c.isalpha())


def anagrams_2():
    arr = [no_spaces_special_characters_nums(input().lower()) for _ in range(2)]
    line_1, line_2 = [sorted(text) for text in arr]
    print('YES' if line_1 == line_2 else 'NO')


def dictionary_synonyms():
    num = int(input())
    dic_syn = dict(input().split() for _ in range(num))
    search = input()
    if search in dic_syn:
        res = dic_syn[search]
    else:
        res = ''.join(k for k, v in dic_syn.items() if search == v)

    print(res)


def countries_cities():
    counter_country = int(input())
    countrys = [input().split() for _ in range(counter_country)]
    counter_city = int(input())
    citys = [input() for _ in range(counter_city)]

    dic_country = {}
    for city in countrys:
        dic_country.setdefault(city[0], city[1:])

    for city in citys:
        for k, v in dic_country.items():
            if city in v:
                print(k)


def phone_book():
    phones_book = {}
    for _ in range(int(input())):
        value, key = input().lower().split()
        if key in phones_book:
            phones_book[key] += [value]
        else:
            phones_book[key] = [value]

    for _ in range(int(input())):
        print(*phones_book.get(input().lower(), ['абонент не найден']))


def secret_word():
    word = input()
    dic_count_char = {}

    for c in word:
        dic_count_char[c] = dic_count_char.get(c, 0) + 1

    mydict = {}
    for _ in range(int(input())):
        key, value = input().split(': ')
        mydict[int(value)] = key

    for c in word:
        # print(mydict[dic_count_char[c]], end='')
        print(mydict[word.count(c)], end='')  # один словарь.

    """
    dct, word = {}, {}
    s = input()
    for c in s:
        word[c] = word.get(c, 0) + 1
    for _ in range(int(input())):
        a, b = input().split(': ')
        dct[int(b)] = a
    for c in s:
        print(dct[word[c]], end='')
    """


def test():
    marks = {
        'class': {
            'student': {
                'name': 'Rosaly',
                'marks': {
                    'physics': 70,
                    'history': 80
                }
            }
        }
    }
    print(marks['class']['student']['marks']['history'])


def insert_test():
    s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

    result = {int(c.split(':')[0]): c.split(':')[1] for c in s.split()}
    # result = {int(k): v for k, v in [l.split(':') for l in s.split()]}
    print(result)


def insert_test_2():
    numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

    result = {}

    for key in numbers:
        print(key)
        for i in range(1, key + 1):
            if key % i == 0:
                result[key] = i

    print(result)


def test_1():
    numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

    result = {val: [i for i in range(1, val + 1) if val % i == 0] for val in numbers}
    # result = {}
    # for val in numbers:
    #     arr = []
    #     for i in range(1, val + 1):
    #         if val % i == 0:
    #             arr.append(i)
    #     result[val] = arr
    #
    # print(result)


def test_2():
    words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

    result = {word: [ord(c) for c in word] for word in words}
    pprint(result)


def test_3():
    letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
               12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
               23: 'X', 24: 'Y', 26: 'Z'}

    remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]

    result = {k: v for k, v in letters.items() if k not in remove_keys}
    print(result)


def test_4():
    students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
                'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
                'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
                'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}

    result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}
    print(result.values())


def test_5():
    tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24),
              (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]

    result = {elem[0]: elem[1:] for elem in tuples}
    print(result)


def insert_test_3():
    student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012',
                   'S013']
    student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
                     'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman',
                     'Tom Hardy']
    student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

    result = [{k: {n: g}} for k, n, g in zip(student_ids, student_names, student_grades)]
    print(result)

    # [ {переменная1:{переменная2: переменная3}} for переменная1, переменная2, переменная3 in zip(список1, список2, список3)]


def control_work_1():
    my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
               'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
               'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
    result = {}
    for k, val in my_dict.items():
        result[k] = []
        for v in val:
            if v <= 20:
                result[k] += [v]
    my_dict = {k: [i for i in v if i <= 20] for k, v in my_dict.items()}
    print(result)


def control_work_2():
    emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
              'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
              'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
              'yandex.ru': ['surface', 'google'],
              'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
              'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

    # for k, vel in emails.items():
    #     for v in vel:
    #         print(v+k)

    result = sorted([v + '@' + k for k, vel in emails.items() for v in vel])
    print(*result, sep='\n')


def control_work_3():
    "Минутка генетики"
    # nucleotide_dna = ['A', 'C', 'G', 'T']

    rna_chain = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    # dna = input()
    dna = 'ACTG'
    # res = ''
    # for c in dna:
    #     if c in rna_chain:
    #         res += rna_chain[c]

    res = [rna_chain[c] for c in dna if c in rna_chain]
    print(*res, sep='')


def control_work_4():
    '''Порядковый номер'''

    line = input().split()
    # line = 'прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон'.split()
    get_dict = {}
    res = []
    for word in line:
        get_dict[word] = get_dict.get(word, 0) + 1
        if get_dict[word] > 0:
            res.append(get_dict[word])

    print(*res)
    """
    for i in s:
        d[i] = d.get(i, 0) + 1
        print(d[i], end = ' ')
    """


def control_work_5():
    '''Scrabble game'''
    d = {
        1: "AEILNORSTU",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }

    # word = input()
    word = 'FRESHENER'
    res = 0
    for c in word:
        for k, v in d.items():
            if c in v:
                res += k
    print(res)
    """
    bill = 0
    for i in input().upper():
        bill += scrable.get(i, scrable[i])
    print(bill)
    """


def control_work_6():
    '''Строка запроса'''

    params = {'name': 'timur', 'age': 28}

    def build_query_string(params):
        arr = []
        # for k, v in params.items():
        #     arr.append(f'{k}={v}')
        # return '&'.join(sorted(arr))
        return '&'.join(sorted([f'{k}={v}' for k, v, in params.items()]))

    res = build_query_string(params)
    print(res)


def control_work_7():
    '''Слияние словарей'''

    values = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]

    def merge(values):  # values - это список словарей
        res = {}
        for d in values:
            for k, v in d.items():
                res.setdefault(k, set()).add(v)

        print(res)

    print(merge(values))


def control_work_8():
    '''Опасный вирус'''

    command = {'write': 'W',
               'read': 'R',
               'execute': 'X'}

    d1 = {}
    for _ in range(int(input())):
        line = input().split()
        d1[line[0]] = line[1:]

    for _ in range(int(input())):
        s = input().split()
        if command[s[0]] in d1[s[1]]:
            print('OK')
        else:
            print('Access denied')



def control_work_9():
    """Покупки в интернет-магазине"""
    n = int(input())
    res = {}
    for _ in range(n):
        a, b, c = input().split()
        c = int(c)

        if a not in res.keys():
            res[a] = res.setdefault(a, {b: c})
        else:
            if b not in res[a]:
                res[a].update({b: c})
            else:
                res[a][b] = res[a].get(b) + c

    for key in sorted(res):
        print(f'{key}:')
        for k, v in sorted(res[key].items()):
            print(k, v)


def main():
    # control_work_9()
    control_work_8()
    # control_work_7()
    # control_work_6()
    # control_work_5()
    # control_work_4()
    # control_work_3()
    # control_work_2()
    # control_work_1()
    # insert_test_3()
    # test_5()
    # test_4()
    # test_3()
    # test_2()
    # test_1()
    # insert_test_2()
    # insert_test()
    # test()
    # secret_word()
    # phone_book()
    # countries_cities()
    # dictionary_synonyms()
    # text = 'afaf : df s'
    # print(no_spaces_special_characters_nums(text))
    # anagrams_2()
    # anagrams_1()
    # programmer_dictionary()
    # fixing_duplicates()
    # rarest_word()
    # test_text_3()
    # text_text_2()
    # test_text()
    # test_1()
    # test()
    # metod_get()
    # morse_code()
    # set_messages()
    # information_training_courses()
    # string_representation()
    # test_1()


if __name__ == '__main__':
    main()
