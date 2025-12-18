from functools import reduce


def sum_fn(a, b): return a + b
def mul_fn(a, b): return a * b


with open('06.txt') as f:
    raw_lines = [line for l in f.readlines() if (line := l.replace('\n', ''))]
    rows = len(raw_lines)


def part1():
    lines = [[n for n in l.split(' ') if n] for l in raw_lines]
    for line in lines[:-1]:
        for i, v in enumerate(line):
            line[i] = int(v)
    ops = [c == '*' for c in lines[-1]]
    rv = 0
    for j, multi in enumerate(ops):
        vals = [lines[i][j] for i in range(rows - 1)]
        rv += reduce(mul_fn if multi else sum_fn, vals, 1 if multi else 0)
    return rv


def part2():
    max_line_len = max(len(l) for l in raw_lines)
    ops = [[c == '*', i] for i, c in enumerate(raw_lines[-1]) if c in ['*', '+']]
    rv = 0
    for i, v in enumerate(ops[:-1]):
        v.append(ops[i + 1][1])
    ops[-1].append(max_line_len)
    for multi, start, end in ops:
        vals = []
        for j in range(start, end):
            v = [c for line in raw_lines[:-1] if j < len(line) and (c := line[j]) != ' ']
            if v:
                vals.append(int(''.join(v)))
        rv += reduce(mul_fn if multi else sum_fn, vals, 1 if multi else 0)
    return rv


print(part1())
print(part2())
