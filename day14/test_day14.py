import day14


def test_calc_simple_load():
    assert day14.calc_tilt_load(list('...')) == 0
    assert day14.calc_tilt_load(list('#..')) == 0
    assert day14.calc_tilt_load(list('O..')) == 3
    assert day14.calc_tilt_load(list('.O.')) == 3
    assert day14.calc_tilt_load(list('..O')) == 3
    assert day14.calc_tilt_load(list('OO.')) == 5
    assert day14.calc_tilt_load(list('OOO')) == 6
    assert day14.calc_tilt_load(list('O#.')) == 3
    assert day14.calc_tilt_load(list('.#O')) == 1
    assert day14.calc_tilt_load(list('#O.')) == 2
    assert day14.calc_tilt_load(list('#.O')) == 2
    assert day14.calc_tilt_load(list('#OO')) == 3
    assert day14.calc_tilt_load(list('#OO')) == 3
    assert day14.calc_tilt_load(list('#O#')) == 2
    assert day14.calc_tilt_load(list('#O#.')) == 3
    assert day14.calc_tilt_load(list('#O#...O')) == 10


def test_calc_load():
    assert day14.calc_load(list('....')) == 0
    assert day14.calc_load(list('...O')) == 1
    assert day14.calc_load(list('O...')) == 4


def test_part1():
    assert day14.part1(input='day14/input_example.txt') == 136
    assert day14.part1(input='day14/input.txt') == 110779


def test_rotate_notes():
    assert day14.rotate_notes([(1, 2), (3, 4)]) == [(3, 1), (4, 2)]
    assert day14.rotate_notes([(3, 1), (4, 2)]) == [(4, 3), (2, 1)]
    assert day14.rotate_notes([(4, 3), (2, 1)]) == [(2, 4), (1, 3)]
    assert day14.rotate_notes([(2, 4), (1, 3)]) == [(1, 2), (3, 4)]

    # now with a rock... ouf!
    assert day14.rotate_notes([('O', '.'), ('.', '.')]) == [
        ('.', 'O'), ('.', '.')]
    assert day14.rotate_notes([('.', 'O'), ('.', '.')]) == [
        ('.', '.'), ('.', 'O')]
    assert day14.rotate_notes([('.', '.'), ('.', 'O')]) == [
        ('.', '.'), ('O', '.')]
    assert day14.rotate_notes([('.', '.'), ('O', '.')]) == [
        ('O', '.'), ('.', '.')]


def test_tilt_note():
    assert day14.tilt_note(('O', '.')) == ('O', '.')
    assert day14.tilt_note(('.', 'O', '.')) == ('O', '.', '.')
    assert day14.tilt_note(('#', 'O', '.')) == ('#', 'O', '.')
    assert day14.tilt_note(('#', '.', 'O')) == ('#', 'O', '.')
    assert day14.tilt_note(('.', '#', 'O')) == ('.', '#', 'O')
    assert day14.tilt_note(('.', '#', '.', 'O')) == ('.', '#', 'O', '.')


def test_part2():
    assert day14.part2() == 86069
