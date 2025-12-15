with open('02.txt') as f:
    ranges = (r.split('-') for r in f.read().strip().split(','))
    ranges = [(int(a), int(b)) for a, b in ranges]


def check(invalid_fn):
    rv = 0
    for r1, r2 in ranges:
        for i in range(r1, r2 + 1):
            if invalid_fn(i):
                rv += i
    return rv


def is_invalid1(num):
    num_str = str(num)
    num_len = len(num_str)
    if num_len % 2 != 0: return False
    return num_str[:num_len // 2] == num_str[num_len // 2:]


def is_invalid2(num):
    num_str = str(num)
    num_len = len(num_str)
    for l in range(1, num_len // 2 + 1):
        if num_len % l != 0: continue
        repeats = num_len // l
        substr = num_str[:l]
        num2 = ''.join([substr] * repeats)
        if num_str == num2:
            return True
    return False


print(check(is_invalid1))
print(check(is_invalid2))
