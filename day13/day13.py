from collections import defaultdict
import math


def get_column(map, index):
    return ''.join([row[index] for row in map])


def get_mirror_lines(map):
    # scan through and keep pairs of indices that have same line
    vert_lines = []
    length_col = len(map[0])

    col_prev = ''
    for c in range(length_col):
        col = get_column(map, c)
        if col == col_prev:
            vert_lines.append((c-1, c))
        col_prev = col

    hor_lines = []
    length_row = len(map)

    row_prev = ''
    for r in range(length_row):
        row = map[r]
        if row == row_prev:
            hor_lines.append((r-1, r))
        row_prev = row

    return [vert_lines, hor_lines]


def generate_mirror_pairs(pair, length):
    pairs = []

    spread = 1
    low = min(pair)
    high = max(pair)

    while (low - spread) >= 0 and (high + spread) <= length-1:
        pairs.append((low-spread, high+spread))
        spread += 1

    return pairs


def get_real_mirror(map):
    verts, hors = get_mirror_lines(map)

    v_result = 0
    if verts:
        for v in verts:
            works = True
            pairs = generate_mirror_pairs(v, len(map[0]))
            for low, high in pairs:
                col_low = get_column(map, low)
                col_high = get_column(map, high)
                if col_low != col_high:
                    works = False
            if works:
                if v_result != 0:
                    raise ValueError('already found one...')
                v_result = max(v)
                break

    h_result = 0
    if hors:
        for h in hors:
            works = True
            pairs = generate_mirror_pairs(h, len(map))
            for low, high in pairs:
                col_low = map[low]
                col_high = map[high]
                if col_low != col_high:
                    works = False
            if works:
                if h_result != 0:
                    raise ValueError('already found one...')
                h_result = max(h)
                break

    return (v_result, h_result)


def get_vert_spread(map):
    spread = defaultdict(list)

    length_col = len(map[0])

    for c in range(length_col):
        col = get_column(map, c)
        spread[col].append(c)

    pairs = []
    loners = []
    to_fix = []
    for key, val in spread.items():
        if len(val) == 2:
            pairs.append(val)
        elif len(val) == 1:
            loners.append(val)
        else:
            to_fix.append(val)

    min_loner = min(loners)[0]
    max_loner = max(loners)[0]

    if to_fix:
        # if we don't mirror at at least 1 edge of map
        if min_loner != 0 and max_loner != length_col:
            pass
        else:
            raise ValueError

    total = 0
    count = 0
    for val in pairs:
        v1 = val[0]
        v2 = val[1]
        r = list(range(min_loner, max_loner+1))
        if v1 and v2 in r:
            continue
        count += 2
        total += sum(val)

    if count > 0:
        return math.ceil(total/count)
    return 0


def get_hor_spread(map):
    spread = defaultdict(list)

    length_row = len(map)

    for r in range(length_row):
        row = map[r]
        spread[row].append(r)

    pairs = []
    loners = []
    to_fix = []
    for key, val in spread.items():
        if len(val) == 2:
            pairs.append(val)
        elif len(val) == 1:
            loners.append(val)
        else:
            to_fix.append(val)

    min_loner = min(loners)[0]
    max_loner = max(loners)[0]

    if to_fix:
        if min_loner <= 1 and max_loner >= length_row-2:
            # if we don't mirror at at least 1 edge of map
            pass
        else:
            for f in to_fix:
                to_fix_max = max(f)
                to_fix_min = min(f)

                below = [i for i in f if i < min_loner]
                above = [i for i in f if i > max_loner]

                if len(above) == 2:
                    pairs.append(above)
                elif len(below) == 2:
                    pairs.append(below)
                elif to_fix_max and (to_fix_max-1) in f:
                    pairs.append([to_fix_max, to_fix_max-1])
                elif to_fix_min and (to_fix_min+1) in to_fix:
                    pairs.append([to_fix_min, to_fix_min+1])
                elif len(f) % 2 == 0:
                    # they aren't loners, assume all pair
                    while f:
                        pairs.append(f[:2])
                        f = f[2:]
                else:
                    raise ValueError

    total = 0
    count = 0
    for val in pairs:
        v1 = val[0]
        v2 = val[1]
        ran = list(range(min_loner, max_loner+1))
        if v1 and v2 in ran:
            continue
        count += 2
        total += sum(val)

    if count > 0:
        return math.ceil(total/count)
    return 0


def part1(input='day13/input.txt'):
    total = 0

    with open(input, 'r') as file:
        _map = []

        for line in file:
            line = line.strip()

            if line:
                _map.append(line)
            else:
                v, h = get_real_mirror(_map)
                total += v
                total += (h*100)
                _map = []

        if _map:
            v, h = get_real_mirror(_map)
            total += v
            total += (h*100)
            _map = []

    return total


def print_array(loop):
    print('')
    for row in loop:
        for i in row:
            print(i, end='')
        print('')


if __name__ == "__main__":
    print(part1())
