ranges = []
available = []
with open('05.txt') as f:
    lines = (line for l in f.readlines() if (line := l.strip()))
    for line in lines:
        if '-' in line:
            l, r = line.split('-')
            ranges.append((int(l), int(r)))
            ranges.sort()
        else:
            available.append(int(line))


def part1():
    return sum(1 for n in available if any(l <= n <= r for l, r in ranges))


def part2():
    rngs1 = ranges
    while True:
        rngs2 = []
        for l1, r1 in rngs1:
            found2 = False
            for i2, (l2, r2) in enumerate(rngs2):
                if l2 <= l1 and r1 <= r2:
                    found2 = True
                    break
                if l1 <= l2 and r2 <= r1:
                    rngs2[i2] = (l1, r1)
                    found2 = True
                    break
                if l1 <= l2 <= r1:
                    rngs2[i2] = (l1, max(r1, r2))
                    found2 = True
                    break
                if l2 <= l1 <= r2:
                    rngs2[i2] = (l2, max(r1, r2))
                    found2 = True
                    break
            if not found2:
                rngs2.append((l1, r1))
        rngs2.sort()
        if rngs1 == rngs2:
            break
        else:
            rngs1 = rngs2
    rv = 0
    for l, r in rngs1:
        assert l <= r
        rv += r - l + 1
    return rv


# print(part1())
print(part2())
