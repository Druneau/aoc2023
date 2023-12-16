import copy


def calc_tilt_load(noted_list):

    cumulative_load = 0

    max_load = len(noted_list)
    cube_load = max_load
    rolling_count = 0

    for i in range(max_load):

        entry = noted_list[i]
        if 'O' == entry:
            rolling_count += 1
        elif '#' == entry:
            for rolling in range(rolling_count):
                this_load = cube_load - rolling
                cumulative_load += this_load

            cube_load = max_load - i - 1
            rolling_count = 0

    if rolling_count > 0:
        # account for remaining rolling rocks!
        for rolling in range(rolling_count):
            this_load = cube_load - rolling
            cumulative_load += this_load

    return cumulative_load


def calc_load(note):
    max_load = len(note)

    cumulative_load = 0

    for i in range(max_load):
        if note[i] == 'O':
            cumulative_load += (max_load-i)

    return cumulative_load


def get_column(map, index):
    return ''.join([row[index] for row in map])


def rotate_notes(notes, clockwise=True):
    if clockwise:
        return list(zip(*notes[::-1]))

    return list(reversed(list(zip(*notes))))


def tilt_notes(notes):
    new_notes = []
    for n in notes:
        new_notes.append(tilt_note(n))
    return new_notes


def tilt_note(note_row):
    new_note = ()
    rolling_count = 0
    space_count = 0

    for i in range(len(note_row)):
        entry = note_row[i]

        if 'O' == entry:
            rolling_count += 1
        elif '.' == entry:
            space_count += 1
        elif '#' == entry:
            new_note += rolling_count * ('O',)
            new_note += space_count * ('.',)
            new_note += ('#',)
            rolling_count = 0
            space_count = 0

    # clear remaining
    new_note += rolling_count * ('O',)
    new_note += space_count * ('.',)

    return new_note


def part1(input='day14/input.txt'):

    dish = []
    with open(input, 'r') as file:

        for line in file:
            line = line.strip()

            if line:
                dish.append(line)

    total = 0

    for i in range(len(dish)):
        col = get_column(dish, i)
        total += calc_tilt_load(col)

    return total


def print_array(loop):
    print('')
    for row in loop:
        for i in row:
            print(i, end='')
        print('')


def part2(input='day14/input.txt'):

    dish = []
    with open(input, 'r') as file:

        for line in file:
            line = line.strip()

            if line:
                dish.append(list(line))

    # align wiht tilt_notes function
    dish = rotate_notes(dish, False)

    loads = []
    cyclic = []
    start_cyclic = -1

    for cycle in range(1, 1000000000):

        for rotate in range(4):
            dish = tilt_notes(dish)
            dish = rotate_notes(dish)

        load = 0

        for i in range(len(dish)):
            load += calc_load(dish[i])

        if load == 86069:
            print('{}, {}'.format(cycle, load))
            if not cyclic:
                start_cyclic = cycle

        if start_cyclic > -1:
            cyclic.append(load)
        loads.append(load)

    index = 1000000000
    position = index % len(cyclic)
    print(len(cyclic))
    projected_value = cyclic[position]

    print(f"The projected value at index {index} is {projected_value}")

    return projected_value


if __name__ == '__main__':
    print(part1())
    print(part2())
