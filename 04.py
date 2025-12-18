with open('04.txt') as f:
    lines = [[c == '@' for c in line] for l in f.readlines() if (line := l.strip())]
rows = len(lines)
cols = len(lines[0])


def remove():
    def count_pos(i, j):
        if not(0 <= i < rows and 0 <= j < cols): return 0
        return 1 if lines[i][j] else 0

    rv = []
    for i, row in enumerate(lines):
        for j, v in enumerate(row):
            if not v: continue
            neighbours = \
                count_pos(i + 1, j + 1) + \
                count_pos(i + 1, j) + \
                count_pos(i + 1, j - 1) + \
                count_pos(i, j + 1) + \
                count_pos(i, j - 1) + \
                count_pos(i - 1, j + 1) + \
                count_pos(i - 1, j) + \
                count_pos(i - 1, j - 1)
            if neighbours < 4:
                rv.append((i, j))
    return rv


def part1():
    return len(remove())


def part2():
    rv = 0
    while to_remove := remove():
        for i, j in to_remove:
            lines[i][j] = False
        rv += len(to_remove)
    return rv


print(part1())
print(part2())

