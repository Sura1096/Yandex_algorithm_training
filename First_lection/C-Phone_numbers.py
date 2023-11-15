'''
Телефонные номера в адресной книге мобильного телефона имеют один из следующих форматов:
+7<код><номер>,
8<код><номер>,
<номер>,
где <номер> — это семь цифр, а <код> — это три цифры или три цифры в круглых скобках.
Если код не указан, то считается, что он равен 495.
Кроме того, в записи телефонного номера может стоять знак “-” между любыми двумя цифрами (см. пример).
На данный момент в адресной книге телефона Васи записано всего три телефонных номера, и он хочет записать туда еще один.
Но он не может понять, не записан ли уже такой номер в телефонной книге.
Помогите ему! Два телефонных номера совпадают, если у них равны коды и равны номера.
Например, +7(916)0123456 и 89160123456 — это один и тот же номер.

Формат ввода
В первой строке входных данных записан номер телефона, который Вася хочет добавить в адресную книгу своего телефона.
В следующих трех строках записаны три номера телефонов, которые уже находятся в адресной книге телефона Васи.
Гарантируется, что каждая из записей соответствует одному из трех приведенных в условии форматов.

Формат вывода
Для каждого телефонного номера в адресной книге выведите YES (заглавными буквами),
если он совпадает с тем телефонным номером, который Вася хочет добавить в адресную книгу
или NO (заглавными буквами) в противном случае.
'''


def compare_len11(add, comp_number):
    if len(comp_number) == 11:
        if comp_number[1:] == add[1:]:
            print('YES')
        else:
            print('NO')
    elif len(comp_number) == 10:
        if add[1:] == comp_number:
            print('YES')
        else:
            print('NO')
    elif len(comp_number) == 7:
        if add[1:4] == '495' and add[4:] == comp_number:
            print('YES')
        else:
            print('NO')


def compare_len10(add, comp_number):
    if len(comp_number) == 11:
        if add == comp_number[1:]:
            print('YES')
        else:
            print('NO')
    elif len(comp_number) == 10:
        if add == comp_number:
            print('YES')
        else:
            print('NO')
    elif len(comp_number) == 7:
        if add[:3] == '495' and add[3:] == comp_number:
            print('YES')
        else:
            print('NO')


def compare_len7(add, comp_number):
    if len(comp_number) == 11:
        if add == comp_number[4:] and comp_number[1:4] == '495':
            print('YES')
        else:
            print('NO')
    elif len(comp_number) == 10:
        if add == comp_number[3:] and comp_number[:3] == '495':
            print('YES')
        else:
            print('NO')
    elif len(comp_number) == 7:
        if add == comp_number:
            print('YES')
        else:
            print('NO')


add_number = input().replace('+', '').replace('(', '').replace(')', '').replace('-', '')
first = input().replace('+', '').replace('(', '').replace(')', '').replace('-', '')
second = input().replace('+', '').replace('(', '').replace(')', '').replace('-', '')
third = input().replace('+', '').replace('(', '').replace(')', '').replace('-', '')

if len(add_number) == 11:
    for el in first, second, third:
        compare_len11(add_number, el)
if len(add_number) == 10:
    for el in first, second, third:
        compare_len10(add_number, el)
if len(add_number) == 7:
    for el in first, second, third:
        compare_len7(add_number, el)
