from pprint import pprint
import re
import sys


CONTAINER_RE = re.compile('(\w+ \w+)(?= bags contain)')
BAGS_RE = re.compile(r'(?:(?:\d+ (\w+ \w+) bag(?:s?)(?:, |.)))')


if __name__ == '__main__':
    # Mapping between <contained bag>: <container bags>
    contained_in = {}

    for line in sys.stdin:
        container = CONTAINER_RE.match(line).group()
        contained_bags = BAGS_RE.findall(line)
        for bag in contained_bag:
            contained_in.setdefault(bag, set()).add(container)

    # Initialize the queue with bags that can contain shiny gold bag
    queue = list(contained_in['shiny gold'])
    visited = set()

    # BFS
    while queue:
        next_bag = queue.pop()
        visited.add(next_bag)
        can_be_contained_in = contained_in.get(next_bag, set())
        to_visit = can_be_contained_in - visited
        queue += list(to_visit)

    print(len(visited))
