import re
import sys


PASSWORD_RE = re.compile('(\d+)-(\d+) (\w): (\w+)')


if __name__ == '__main__':
    correct_count = 0
    for line in sys.stdin:
        min_count, max_count, letter, password = PASSWORD_RE.match(line).groups()
        min_count = int(min_count)
        max_count = int(max_count)
        letter_count = len(re.findall(letter, password))

        if min_count <= letter_count <= max_count:
            correct_count += 1
    print(correct_count)
