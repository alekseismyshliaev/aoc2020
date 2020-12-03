import sys


TREE_SPACE = '#'
FREE_SPACE = '.'

DX = 3
DY = 1

def count_trees(map_data, dx, dy):
    '''Count how many trees you encounter while traversing at the given slope

    :param map_data: list of strings, describing one column of the map.
        the map repeats horizontally.
    :param dx: slope of the travel, horizontal (integer steps)
    :param dy: slope of the travel, vertical (integer steps)
    :returns: number of the tree spaces encountered on this slope
    '''
    xx = 0
    yy = 0
    tree_count = 0

    while yy < len(map_data):
        if map_data[yy][xx] == TREE_SPACE:
            tree_count += 1
        xx = (xx + dx) % len(map_data[yy])
        yy += dy

    return tree_count

if __name__ == '__main__':
    travel_map = []
    for line in sys.stdin:
        travel_map.append(line.rstrip('\n'))

    tree_count = count_trees(travel_map, 3, 1)

    print(tree_count)
