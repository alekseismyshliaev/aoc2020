import sys


TREE_SPACE = '#'
FREE_SPACE = '.'

DX = 3
DY = 1


if __name__ == '__main__':
    travel_map = []
    for line in sys.stdin:
        travel_map.append(line.rstrip('\n'))

    xx = 0
    yy = 0

    tree_count = 0
    
    while yy < len(travel_map):
        if travel_map[yy][xx] == TREE_SPACE:
            tree_count += 1

        xx = (xx + DX) % len(travel_map[yy])
        yy += DY

    print(tree_count)
