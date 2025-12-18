with open('03.txt') as f:
    lines = (line for l in f.readlines() if (line := l.strip()))
    lines = [[int(c) for c in l] for l in lines]


def part1():
    rv = 0
    for line in lines:
        max1 = max(line[:-1])
        i1 = line.index(max1)
        max2 = max(line[i1 + 1:])
        rv += int(str(max1) + str(max2))
    return rv


def part2():
    rv = 0
    for line in lines:
        maxs = []
        start = 0
        for i in range(12):
            end = len(line) - (12 - i - 1)
            subl = line[start:end]
            max1 = max(subl)
            start += subl.index(max1) + 1
            maxs.append(str(max1))
        rv += int(''.join(maxs))
    return rv

print(part1())
print(part2())

