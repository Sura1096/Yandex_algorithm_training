'''
В данном списке из n ≤ 105 целых чисел найдите три числа,произведение которых максимально.
Решение должно иметь сложность O(n), где n - размер списка.
Выведите три искомых числа в любом порядке.
'''


def greatest_product_of_two(nums):
    nums = list(map(int, nums.split()))

    maxi1, maxi2, maxi3 = float('-inf'), float('-inf'), float('-inf')
    mini1, mini2 = float('inf'), float('inf')

    for ind, num in enumerate(nums):
        if num > maxi1:
            maxi3 = maxi2
            maxi2 = maxi1
            maxi1 = num
        elif num > maxi2:
            maxi3 = maxi2
            maxi2 = num
        elif num > maxi3:
            maxi3 = num

        if num < mini1:
            mini2 = mini1
            mini1 = num
        elif num < mini2:
            mini2 = num

    if maxi1 * maxi2 * maxi3 < mini1 * mini2 * maxi1:
        return str(mini1) + ' ' + str(mini2) + ' ' + str(maxi1)
    else:
        return str(maxi1) + ' ' + str(maxi2) + ' ' + str(maxi3)


n = input()
print(greatest_product_of_two(n))
