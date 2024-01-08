'''
В данном списке из n ≤ 105 целых чисел найдите три числа,произведение которых максимально.
Решение должно иметь сложность O(n), где n - размер списка.
Выведите три искомых числа в любом порядке.
'''

# TODO:
# 1. You wanted to divide into two parts greatest_product_of_three function

# 2. You can use index() function instead of using 4 variables in
# which you store indexes of maxi1, maxi2, mini1, mini2

# 3. Your solution is incorrect and didn't pass all testcases


def greatest_product_of_two(nums):
    pass


def greatest_product_of_three(nums):
    nums = list(map(int, nums.split()))

    maxi1, maxi2 = float('-inf'), float('-inf')
    mini1, mini2 = float('inf'), float('inf')

    maxi_ind1 = None
    maxi_ind2 = None
    mini_ind1 = None
    mini_ind2 = None

    for ind, num in enumerate(nums):
        if num > maxi1:
            maxi_ind2 = maxi_ind1
            maxi_ind1 = ind
            maxi2 = maxi1
            maxi1 = num
        elif num > maxi2:
            maxi_ind2 = ind
            maxi2 = num

        if num < mini1:
            mini_ind2 = mini_ind1
            mini_ind1 = ind
            mini2 = mini1
            mini1 = num
        elif num < mini2:
            mini_ind2 = ind
            mini2 = num

    if maxi1 * maxi2 > mini1 * mini2:
        product = maxi1 * maxi2 * nums[0]
        third = nums[0]

        for ind in range(1, len(nums)):
            if (ind != maxi_ind1 and ind != maxi_ind2) and (product < maxi1 * maxi2 * nums[ind]):
                product = maxi1 * maxi2 * nums[ind]
                third = nums[ind]

        return str(maxi1) + ' ' + str(maxi2) + ' ' + str(third)

    else:
        product = mini1 * mini2 * nums[0]
        third = nums[0]

        for ind in range(1, len(nums)):
            if (ind != mini_ind1 and ind != mini_ind2) and (product < mini1 * mini2 * nums[ind]):
                product = mini1 * mini2 * nums[ind]
                third = nums[ind]

        return str(mini1) + ' ' + str(mini2) + ' ' + str(third)


n = input()
print(greatest_product_of_three(n))