import day18
import pytest


@pytest.fixture
def input_example():
    lines = """
    R 6 (#70c710)
    D 5 (#0dc571)
    L 2 (#5713f0)
    D 2 (#d2c081)
    R 2 (#59c680)
    D 2 (#411b91)
    L 5 (#8ceee2)
    U 2 (#caa173)
    L 1 (#1b58a2)
    U 2 (#caa171)
    R 2 (#7807d2)
    U 3 (#a77fa3)
    L 2 (#015232)
    U 2 (#7a21e3)
    """
    lines = [line.strip() for line in lines.strip().split('\n')]
    return lines


@pytest.fixture
def input_negatives():
    lines = """
    L 5 (#70c710)
    U 5 (#70c710)
    R 5 (#70c710)
    R 5 (#70c710)
    D 5 (#70c710)
    L 5 (#70c710)
    """
    lines = [line.strip() for line in lines.strip().split('\n')]
    return lines


@pytest.fixture
def trench_loop_example():
    loop = ['#######',
            '#.....#',
            '###...#',
            '..#...#',
            '..#...#',
            '###.###',
            '#...#..',
            '##..###',
            '.#....#',
            '.######']
    return [list(l) for l in loop]


@pytest.fixture
def trench_fill_example():
    loop = ['#######',
            '#######',
            '#######',
            '..#####',
            '..#####',
            '#######',
            '#####..',
            '#######',
            '.######',
            '.######']
    return [list(l) for l in loop]


@pytest.fixture
def lagoon_edges(input_example):
    lines = day18.generate_translated_lines(input_example)
    size = day18.get_lagoon_size_from_lines(lines)
    return day18.trench_lagoon_edges(lines, size)


def test_generate_line():
    assert day18.generate_line('R 6 (#70c710)') == ((1, 0), (6, 0))
    assert day18.generate_line('L 6 (#70c710)') == ((-1, 0), (-6, 0))
    assert day18.generate_line('U 3 (#70c710)') == ((0, -1), (0, -3))
    assert day18.generate_line('D 5 (#70c710)') == ((0, 1), (0, 5))


def test_translate_line():
    line = ((1, 0), (6, 0))
    offset = (1, 1)
    assert day18.translate_line(line, offset) == ((2, 1), (7, 1))
    offset = (-1, -1)
    assert day18.translate_line(line, offset) == ((0, -1), (5, -1))


def test_generate_line_list(input_example):
    three_items = input_example[:3]
    assert day18.generate_translated_lines(three_items, (0, 0)) == [
        ((1, 0), (6, 0)), ((6, 1), (6, 5)), ((5, 5), (4, 5))]


def test_get_lagoon_size_from_lines(input_example):
    lines = day18.generate_translated_lines(input_example)
    assert day18.get_lagoon_size_from_lines(lines) == (7, 10)


def test_trench_lagoon_edges(input_example, trench_loop_example):
    lines = day18.generate_translated_lines(input_example)
    size = day18.get_lagoon_size_from_lines(lines)
    lagoon = day18.trench_lagoon_edges(lines, size)

    assert lagoon == trench_loop_example

    assert day18.count_cubic_meters(lagoon) == 38


def test_lagoon_negative(input_negatives):
    lines = day18.generate_translated_lines(input_negatives)

    size = day18.get_lagoon_size_from_lines(lines)

    assert size == (11, 6)

    lines = day18.offset_lines(lines)

    lagoon = day18.trench_lagoon_edges(lines, size)
    day18.flood_fill(lagoon, 1, 1)

    assert day18.count_cubic_meters(lagoon) == 66


def test_dig_lagoon_trench(lagoon_edges, trench_fill_example):
    assert day18.dig_lagoon(lagoon_edges) == trench_fill_example


def test_part1():
    # assert day18.part1('day18/input_example.txt') == 62
    assert day18.part1() == 62
