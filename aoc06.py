import sys


if __name__ == '__main__':
    groups = sys.stdin.read().strip().split('\n\n')

    groups = [group.split('\n') for group in groups]
    all_answers = []
    for group in groups:
        answers = set(group[0])
        for other in group[1:]:
            answers = answers.intersection(set(other))
        all_answers.append(answers)
    print(sum(len(answers) for answers in all_answers))
