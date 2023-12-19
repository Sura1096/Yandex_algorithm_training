'''
A. Возрастает ли список?

Дан список.
Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка больше предыдущего).
Выведите YES, если массив монотонно возрастает и NO в противном случае.

Пример 1
Ввод
1 7 9
Вывод
YES

Пример 2
Ввод
1 9 7
Вывод
NO

Пример 3
Ввод
2 2 2
Вывод
NO
'''


def list_increase(lst):
    result = 'YES'
    for ind in range(1, len(lst)):
        if lst[ind-1] >= lst[ind]:
            result = 'NO'
            break
    return result


lst = list(map(int, input().split()))
print(list_increase(lst))