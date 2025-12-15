with open('01.txt') as f:
    lines = (line for l in f.readlines() if (line := l.strip()))
    lines = [(1 if l[0] == 'R' else -1) * int(l[1:]) for l in lines]


def part1():
    zeros = 0
    pos = 50
    for line in lines:
        pos += line
        pos %= 100
        if pos == 0: zeros += 1
    return zeros


def part2():
    zeros = 0
    pos = 50
    for line in lines:
        zerosl = abs(line) // 100
        zeros += zerosl
        line2 = line % 100 if line > 0 else (line % 100 - 100)
        line = line2
        if line == 0: continue
        pos2 = pos + line
        if pos2 <= 0 < pos:
            zeros += 1
        elif pos2 >= 100:
            zeros += 1
        pos = pos2 % 100
    return zeros


print(part1())
print(part2())
