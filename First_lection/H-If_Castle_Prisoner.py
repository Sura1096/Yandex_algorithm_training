'''
За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D × E.
Замок Иф сложен из кирпичей, размером A × B × C.
Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие,
если стороны кирпича должны быть параллельны сторонам отверстия.

Формат ввода
Программа получает на вход числа A, B, C, D, E.

Формат вывода
Программа должна вывести слово YES или NO.
'''


def is_fit(A, B, C, D, E):
    mini_side = min(D, E)
    maxi_side = max(D, E)

    if mini_side >= min(A, B) and maxi_side >= max(A, B):
        return 'YES'
    elif mini_side >= min(A, C) and maxi_side >= max(A, C):
        return 'YES'
    elif mini_side >= min(C, B) and maxi_side >= max(C, B):
        return 'YES'
    else:
        return 'NO'


A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
print(is_fit(A, B, C, D, E))
