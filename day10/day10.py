from Direction import Direction


def get_pipe_exit(pipe_shape, entry):
    if pipe_shape == '|':
        if entry == Direction.NORTH:
            return Direction.SOUTH
        elif entry == Direction.SOUTH:
            return Direction.NORTH
    elif pipe_shape == '-':
        if entry == Direction.WEST:
            return Direction.EAST
        elif entry == Direction.EAST:
            return Direction.WEST
    elif pipe_shape == 'L':
        if entry == Direction.NORTH:
            return Direction.EAST
        elif entry == Direction.EAST:
            return Direction.NORTH
    elif pipe_shape == 'J':
        if entry == Direction.WEST:
            return Direction.NORTH
        elif entry == Direction.NORTH:
            return Direction.WEST
    elif pipe_shape == '7':
        if entry == Direction.WEST:
            return Direction.SOUTH
        elif entry == Direction.SOUTH:
            return Direction.WEST
    elif pipe_shape == 'F':
        if entry == Direction.SOUTH:
            return Direction.EAST
        elif entry == Direction.EAST:
            return Direction.SOUTH
    return Direction.NONE


def can_enter_pipe(pipe_shape, entry):
    if pipe_shape == '|':
        if entry == Direction.NORTH:
            return True
        elif entry == Direction.SOUTH:
            return True
    elif pipe_shape == '-':
        if entry == Direction.WEST:
            return True
        elif entry == Direction.EAST:
            return True
    elif pipe_shape == 'L':
        if entry == Direction.SOUTH:
            return True
        elif entry == Direction.WEST:
            return True
    elif pipe_shape == 'J':
        if entry == Direction.EAST:
            return True
        elif entry == Direction.SOUTH:
            return True
    elif pipe_shape == '7':
        if entry == Direction.EAST:
            return True
        elif entry == Direction.NORTH:
            return True
    elif pipe_shape == 'F':
        if entry == Direction.NORTH:
            return True
        elif entry == Direction.WEST:
            return True
    return False


def get_possible_exit_directions(adjacents):

    exits = []

    for dir, shape in adjacents:

        if can_enter_pipe(shape, dir):
            exits.append(dir)

    return exits


def load(input):
    array2D = []

    with open(input, 'r') as f:
        for line in f.readlines():
            array2D.append(list(line.strip()))

    return array2D


def get_start_location(_map, symbol='S'):
    row_count = 0
    index = 0

    for row in _map:
        try:
            index = row.index(symbol)
            break
        except ValueError:
            pass
        row_count += 1

    return (row_count, index)


def move(current_location, exit_direction):
    exit_offset = exit_direction.value
    return (current_location[0]+exit_offset[0],
            current_location[1]+exit_offset[1])


def get_symbol_if_exists(_map, location):

    row_index, col_index = location

    if (row_index or col_index) < 0:
        return '.'

    if len(_map) <= row_index:
        return '.'

    if len(_map[0]) <= col_index:
        return 0

    return _map[row_index][col_index]


def print_array(loop):
    print('')
    print('Loop Below!')
    for row in loop:
        for i in row:
            print(i, end='')
        print('')


def part1(input='day10/input'):
    steps = 0

    _map = load(input)
    loop = zeros = [['O' for i in range(139)] for j in range(139)]

    current_location = get_start_location(_map)

    # we'll take the first step before the loop
    start_adjacents = []

    north_location = move(current_location, Direction.NORTH)
    north_symbol = get_symbol_if_exists(_map, north_location)
    start_adjacents.append((Direction.NORTH, north_symbol))

    east_location = move(current_location, Direction.EAST)
    east_symbol = get_symbol_if_exists(_map, east_location)
    start_adjacents.append((Direction.EAST, east_symbol))

    south_location = move(current_location, Direction.SOUTH)
    south_symbol = get_symbol_if_exists(_map, south_location)
    start_adjacents.append((Direction.SOUTH, south_symbol))

    west_location = move(current_location, Direction.WEST)
    west_symbol = get_symbol_if_exists(_map, west_location)
    start_adjacents.append((Direction.WEST, west_symbol))

    exits = get_possible_exit_directions(start_adjacents)

    current_location = move(current_location, exits[0])

    current_symbol = get_symbol_if_exists(_map, current_location)

    steps = 1

    next_dir = exits[0]

    while current_symbol != 'S':
        next_dir = get_pipe_exit(current_symbol, reverse_direction(next_dir))
        current_location = move(current_location, next_dir)
        current_symbol = get_symbol_if_exists(_map, current_location)

        loop[current_location[0]][current_location[1]] = '+'

        steps += 1

    print_array(loop)

    return steps/2


def part2(input='day10/output'):
    _map = load(input)

    area = 0
    for row in _map:
        for i in row:
            if i == '.':
                area += 1
    return area


def reverse_direction(dir):
    if dir == Direction.NORTH:
        return Direction.SOUTH
    if dir == Direction.SOUTH:
        return Direction.NORTH
    if dir == Direction.WEST:
        return Direction.EAST
    if dir == Direction.EAST:
        return Direction.WEST


if __name__ == '__main__':
    print(part1())
    print(part2())
