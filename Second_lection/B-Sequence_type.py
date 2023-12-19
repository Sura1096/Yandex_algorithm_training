'''
По последовательности чисел во входных данных определите ее вид:
CONSTANT – последовательность состоит из одинаковых значений
ASCENDING – последовательность является строго возрастающей
WEAKLY ASCENDING – последовательность является нестрого возрастающей
DESCENDING – последовательность является строго убывающей
WEAKLY DESCENDING – последовательность является нестрого убывающей
RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов

Формат ввода
По одному на строке поступают числа последовательности ai, |ai| ≤ 10^9.
Признаком окончания последовательности является число -2× 10^9. Оно в последовательность не входит.

Формат вывода
В единственной строке выведите тип последовательности.

Пример:
Ввод:
-530
-530
-530
-530
-530
-530
-2000000000

Вывод:
CONSTANT
'''


def weakly_seq(nums):
    seq_type = None

    for ind in range(1, len(nums)):
        if nums[ind - 1] < nums[ind]:
            if seq_type is None:
                seq_type = 'WEAKLY ASCENDING'
            elif seq_type == 'WEAKLY DESCENDING':
                seq_type = 'RANDOM'
                break
        elif nums[ind - 1] > nums[ind]:
            if seq_type is None:
                seq_type = 'WEAKLY DESCENDING'
            elif seq_type == 'WEAKLY ASCENDING':
                seq_type = 'RANDOM'
                break

    return seq_type


def not_weakly_seq(nums):
    seq_type = None

    for ind in range(1, len(nums)):
        if nums[ind - 1] < nums[ind]:
            if seq_type is None:
                seq_type = 'ASCENDING'
            elif seq_type == 'DESCENDING':
                seq_type = 'RANDOM'
                break
        elif nums[ind - 1] > nums[ind]:
            if seq_type is None:
                seq_type = 'DESCENDING'
            elif seq_type == 'ASCENDING':
                seq_type = 'RANDOM'
                break

    return seq_type


def sequence_type():
    pass


print(sequence_type())