from typing import Tuple, List

from draw_trench import print_array

import time

import matplotlib.pyplot as plt


def scale_tuple(coordinate, scale_factor):
    return tuple([scale_factor*x for x in coordinate])


def get_vector(direction_char):
    if direction_char == 'U':
        return (0, -1)
    if direction_char == 'D':
        return (0, 1)
    if direction_char == 'L':
        return (-1, 0)
    if direction_char == 'R':
        return (1, 0)


def generate_line(line_string: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    dir, count, color = line_string.split()
    count = int(count)
    start = get_vector(dir)
    end = scale_tuple(start, count)

    return (start, end)


def translate_line(line: Tuple[Tuple[int, int]], offset: Tuple[int, int]):
    return tuple([(x+dx, y+dy) for x, y in line for dx, dy in [offset]])


def offset_lines(lines):
    min_x = min(min(x for x, y in line) for line in lines)
    min_y = min(min(y for x, y in line) for line in lines)

    offset = (-min_x, -min_y)

    return [translate_line(line, offset) for line in lines]


def generate_translated_lines(line_strings: List[str], start: Tuple[int, int] = (0, 0)):
    lines = [generate_line(l) for l in line_strings]

    translated_lines = []
    for l in lines:
        translated_lines.append(translate_line(l, start))
        start = translated_lines[-1][1]

    return translated_lines


def get_lagoon_size_from_lines(lines: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> Tuple[int, int]:
    bound_left = min(line[0][0] for line in lines)
    bound_right = max(line[0][0] for line in lines)
    bound_down = max(line[1][1] for line in lines)
    bound_up = min(line[1][1] for line in lines)
    width = bound_right - bound_left
    height = bound_down - bound_up
    return ((width+1, height+1))


def trench_line(lagoon, line):
    (x1, y1), (x2, y2) = line

    # If the line is vertical
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            lagoon[y][x1] = '#'
    # If the line is horizontal
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            lagoon[y1][x] = '#'
    return lagoon


def trench_lagoon_edges(lines, size) -> List[List[str]]:
    width, height = size
    lagoon = [['.' for _ in range(width)] for _ in range(height)]

    for l in lines:
        lagoon = trench_line(lagoon, l)

    return lagoon


def flood_fill_recursive(lagoon, x, y, animate=False):
    # If the current cell is not a '.', return
    if lagoon[x][y] != '.':
        return

    # Replace the '.' character with a '#'
    lagoon[x][y] = '#'

    if animate:
        print_array(lagoon)
        time.sleep(0.01)

    # Recursively call flood_fill on all adjacent cells
    if x > 0:
        flood_fill(lagoon, x - 1, y, animate)
    if y > 0:
        flood_fill(lagoon, x, y - 1, animate)
    if x < len(lagoon) - 1:
        flood_fill(lagoon, x + 1, y, animate)
    if y < len(lagoon[0]) - 1:
        flood_fill(lagoon, x, y + 1, animate)


def flood_fill(lagoon, x, y, animate=False):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if lagoon[x][y] != '.':
            continue

        lagoon[x][y] = '#'

        if animate:
            print_array(lagoon)

        if x > 0:
            stack.append((x - 1, y))
        if y > 0:
            stack.append((x, y - 1))
        if x < len(lagoon) - 1:
            stack.append((x + 1, y))
        if y < len(lagoon[0]) - 1:
            stack.append((x, y + 1))


def dig_lagoon(lagoon):

    flood_fill(lagoon, 1, 1)
    return lagoon


def plot(lines):
    for line in lines:
        x_values = [point[0] for point in line]
        y_values = [point[1] for point in line]
        plt.plot(x_values, y_values)

    plt.show()


def count_cubic_meters(lagoon):
    return sum(l.count('#') for l in lagoon)


def part1(input='day18/input.txt', animate=False):
    with open(input, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    lines = generate_translated_lines(lines)

    lines = offset_lines(lines)

    plot(lines)

    size = get_lagoon_size_from_lines(lines)
    lagoon = trench_lagoon_edges(lines, size)

    flood_fill(lagoon, 100, 100, animate)

    return count_cubic_meters(lagoon)


if __name__ == '__main__':
    print(part1(animate=True))
