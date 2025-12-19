from collections import defaultdict
from doctest import UnexpectedException

with open('08.txt') as f:
    lines = (line for l in f.readlines() if (line := l.strip()))
    lines = (line.split(',') for line in lines)
    boxes: list[tuple[int, int, int]] = [tuple(map(int, line)) for line in lines]
    dists = []
    for i, box1 in enumerate(boxes):
        for box2 in boxes[i + 1:]:
            dist = (box2[0] - box1[0]) ** 2 + (box2[1] - box1[1]) ** 2 + (box2[2] - box1[2]) ** 2
            dists.append((dist, box1, box2))
    dists.sort()


class BoxConnector:
    def __init__(self):
        self.next_id = 0
        self.circuits = {}
        self.circuits_reverse = defaultdict(set)

    def connect(self, box1, box2):
        id1 = self.circuits.get(box1, None)
        id2 = self.circuits.get(box2, None)
        if id1 is None and id2 is None:
            self.next_id += 1
            self.circuits[box1] = self.next_id
            self.circuits[box2] = self.next_id
            self.circuits_reverse[self.next_id].add(box1)
            self.circuits_reverse[self.next_id].add(box2)
        elif id1 is None:
            self.circuits[box1] = id2
            self.circuits_reverse[id2].add(box1)
        elif id2 is None:
            self.circuits[box2] = id1
            self.circuits_reverse[id1].add(box2)
        elif id1 == id2:
            pass
        else:
            for box3 in self.circuits_reverse[id2]:
                self.circuits[box3] = id1
                self.circuits_reverse[id1].add(box3)
            del self.circuits_reverse[id2]


def part1():
    connector = BoxConnector()
    for d, box1, box2 in dists[:1000]:
        connector.connect(box1, box2)
    circuits_size = [len(circuit) for circuit in connector.circuits_reverse.values()]
    circuits_size.sort(reverse=True)
    return circuits_size[0] * circuits_size[1] * circuits_size[2]


def part2():
    connector = BoxConnector()
    for d, box1, box2 in dists:
        connector.connect(box1, box2)
        if len(connector.circuits) == len(boxes) and len(connector.circuits_reverse) == 1:
            return box1[0] * box2[0]
    raise UnexpectedException('Should not reach here')


print(part1())
print(part2())

