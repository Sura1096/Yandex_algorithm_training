'''
Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых максимально.
Выведите эти числа в порядке неубывания.
Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.
Решение должно иметь сложность O(n), где n - размер списка.

ПРИМЕР 1
Ввод
4 3 5 2 5

Вывод
5 5


ПРИМЕР 2
Ввод
-4 3 -5 2 5

Вывод
-5 -4
'''


def greatest_product_of_two():
    nums = list(map(int, input().split()))
    
    maxi1 = float('-inf')
    maxi2 = float('-inf')
    mini1 = float('inf')
    mini2 = float('inf')
    for num in nums:
        if num > maxi1:
            maxi2 = maxi1
            maxi1 = num
        elif num > maxi2:
            maxi2 = num
        if num < mini1:
            mini2 = mini1
            mini1 = num
        elif num < mini2:
            mini2 = num

    if maxi1 * maxi2 > mini1 * mini2:
        return str(maxi2) + ' ' + str(maxi1)
    else:
        return str(mini1) + ' ' + str(mini2)


print(greatest_product_of_two())