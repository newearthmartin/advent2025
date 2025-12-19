with open('07.txt') as f:
    lines = [line for l in f.readlines() if (line := l.strip())]
    splitters = set()
    for i, row in enumerate(lines):
        for j, v in enumerate(row):
            if v == 'S':
                si, sj = i, j
            elif v == '^':
                splitters.add((i, j))
    rows = len(lines)


def part1():
    rays = {(si, sj)}
    hit = set()
    while rays:
        new_rays = set()
        for i, j in rays:
            i += 1
            if i >= rows: continue
            if (i, j) in splitters:
                hit.add((i, j))
                new_rays.add((i, j - 1))
                new_rays.add((i, j + 1))
            else:
                new_rays.add((i, j))
        rays = new_rays
    return len(hit)


def part2():
    return get_timelines_for(si, sj, {})


def get_timelines_for(i, j, cache):
    cache_key = (i, j)
    if cache_key in cache: return cache[cache_key]
    if i >= rows:
        rv = 1
    elif lines[i][j] == '^':
        rv = get_timelines_for(i, j - 1, cache) + get_timelines_for(i, j + 1, cache)
    else:
        rv = get_timelines_for(i + 1, j, cache)
    cache[cache_key] = rv
    return rv


print(part1())
print(part2())

