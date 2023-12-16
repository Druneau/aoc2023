import day13
import pytest


@pytest.fixture
def map_vert():
    _map = ['#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.']
    return _map


@pytest.fixture
def map_horz():
    return ['#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#']


@pytest.fixture
def map_vert_special():
    return ['...##..##....',
            '..##....##...',
            '#.#..##....##',
            '##..####..###',
            '...######....',
            '##...##...###',
            '.#.#....#.#..',
            '.#.##..##.#..',
            '...#.##.#....',
            '##.######.###',
            '#..######..##']


def test_get_column(map_vert):
    assert day13.get_column(map_vert, 2) == '##..###'


def test_ger_vert_spread(map_vert, map_vert_special):
    assert day13.get_vert_spread(map_vert) == 5
    assert day13.get_vert_spread(map_vert_special) == 6


def test_get_hor_spread(map_horz):
    assert day13.get_hor_spread(map_horz) == 4


def test_get_mirror_lines(map_horz, map_vert, map_vert_special):
    assert day13.get_mirror_lines(map_horz) == [[(2, 3), (6, 7)], [(3, 4)]]
    assert day13.get_mirror_lines(map_vert) == [[(4, 5)], [(2, 3)]]
    assert day13.get_mirror_lines(map_vert_special) == [[(5, 6), (11, 12)], []]


def test_get_mirror_line(map_horz, map_vert, map_vert_special):
    assert day13.get_real_mirror(map_horz) == (0, 4)
    assert day13.get_real_mirror(map_vert) == (5, 0)
    assert day13.get_real_mirror(map_vert_special) == (12, 0)


def test_failure():
    m = ['##.#.#.',
         '#...##.',
         '..##.##',
         '..##.#.',
         '#...##.',
         '#..#..#',
         '#..#.##',
         '#..#.##',
         '#..#..#',
         '#...##.',
         '..##.#.',
         '..##.##',
         '#...##.']

    assert day13.get_real_mirror(m) == (0, 7)


def test_generate_mirror_pairs():
    assert day13.generate_mirror_pairs((0, 1), length=6) == []
    assert day13.generate_mirror_pairs((1, 2), length=6) == [(0, 3)]
    assert day13.generate_mirror_pairs((2, 3), length=6) == [(1, 4), (0, 5)]
    assert day13.generate_mirror_pairs((3, 4), length=6) == [(2, 5)]
    assert day13.generate_mirror_pairs((4, 5), length=6) == []


def test_part1():
    assert day13.part1('day13/input_example.txt') == 405
    assert day13.part1('day13/input.txt') == 29165


def test_part2():
    assert day13.part2('day13/input_example.txt') == 400
    assert day13.part2('day13/input_debug.txt') == 7
    assert day13.part2('day13/input.txt') == 32192
