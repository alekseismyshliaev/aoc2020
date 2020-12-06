import sys


if __name__ == '__main__':
    groups = sys.stdin.read().strip().split('\n\n')

    groups = [''.join(set(group.replace('\n', ''))) for group in groups]
    print(sum(len(group) for group in groups))
