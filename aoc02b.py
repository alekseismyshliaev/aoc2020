import re
import sys


PASSWORD_RE = re.compile('(\d+)-(\d+) (\w): (\w+)')


if __name__ == '__main__':
    correct_count = 0
    for line in sys.stdin:
        pos1, pos2, letter, password = PASSWORD_RE.match(line).groups()
        pos1 = int(pos1) - 1
        pos2 = int(pos2) - 1

        if (letter == password[pos1]) ^ (letter == password[pos2]):
            correct_count += 1
    print(correct_count)
