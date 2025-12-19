with open('09.txt') as f:
    red_tiles = (line.split(',') for l in f.readlines() if (line := l.strip()))
    red_tiles = [tuple(map(int, line)) for line in red_tiles]
    red_tiles = [(j, i) for i, j in red_tiles]  # need to mirror it to have same as problem description
    red_tiles_set = set(red_tiles)
    green_tiles_set = set()
    rows = max(i for i, _ in red_tiles) + 2
    cols = max(j for _, j in red_tiles) + 2


def part1():
    max_area = 0
    for i, p1 in enumerate(red_tiles):
        i1, j1 = p1
        for p2 in red_tiles[i + 1:]:
            i2, j2 = p2
            area = (abs(i2 - i1) + 1) * (abs(j2 - j1) + 1)
            if area > max_area:
                max_area = area
    return max_area


def part2():
    lines = []
    for i, p1 in enumerate(red_tiles):
        p2 = red_tiles[(i + 1) % len(red_tiles)]
        lines.append((p1, p2, p1[0] == p2[0]))
    lines.sort(key=lambda e: (e[2], (e[0][1], e[0][0]), (e[1][1], e[1][0])))

    for p1, p2, horizontal in lines:
        i1, j1 = p1
        i2, j2 = p2
        inci = (i2 - i1) // abs(i2 - i1) if not horizontal else 0
        incj = (j2 - j1) // abs(j2 - j1) if horizontal else 0
        p = pi, pj = i1, j1
        while pi != i2 or pj != j2:
            if p not in red_tiles_set: green_tiles_set.add(p)
            p = pi, pj = pi + inci, pj + incj
    print_grid()

    vertical_lines = [l for l in lines if not l[2]]
    for i in range(rows):
        vlines = {l[0][1] for l in vertical_lines if min(l[0][0], l[1][0]) <= i <= max(l[0][0], l[1][0])}
        print(i, vlines)
    print(vertical_lines)

    return 0


def print_grid():
    for i in range(rows):
        for j in range(cols):
            p = i, j
            if p in red_tiles_set:
                c = '#'
            elif p in green_tiles_set:
                c = 'X'
            else:
                c = '.'
            print(c, end='')
        print()


# print(part1())
print(part2())

