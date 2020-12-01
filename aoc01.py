import sys


def find_sum_2020(numbers):
    ''' Return two numbers that add up to 2020 '''
    for ii in range(len(numbers)):
        for jj in range(ii + 1, len(numbers)):
            if numbers[ii] + numbers[jj] == 2020:
                return numbers[ii], numbers[jj]
    raise ValueError('given list doesn\'t contain a pair of integers adding up to 2020')


if __name__ == '__main__':
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))
        
    aa, bb = find_sum_2020(numbers)
    print(aa * bb)
