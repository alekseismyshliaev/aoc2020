from functools import reduce
import sys


def find_sum_to(numbers, amount=1, total=0):
    '''
    Return an amount of numbers from the given list that add up to the desired total

    :param numbers: list of numbers to select from
    :param amount: how many numbers to choose
    :param total: what is the desired sum
    :returns: list with all individual numbers that add up to total
    '''
    if not amount:
        return []

    for ii in range(len(numbers)):
        result = []
        num = numbers[ii]
        remainder = total - num
        if amount == 1:
            if remainder == 0:
                return [num]
        else:
            others = find_sum_to(numbers[ii + 1:], amount - 1, remainder)
            if others:
                return [num] + others
    return []


if __name__ == '__main__':
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))

    AMOUNT = 3
    TOTAL = 2020

    result = find_sum_to(numbers, AMOUNT, TOTAL)
    
    if not result:
        raise ValueError(f'could not find {AMOUNT} numbers that add up to {TOTAL}')

    print(result)
    print(reduce(lambda a, b: a*b, result, 1))
