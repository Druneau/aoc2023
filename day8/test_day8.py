from day8 import Directions, part1, parse_node, part2


def test_parse_node():
    assert parse_node('AAA = (BBB, CCC)') == {'AAA': ('BBB', 'CCC')}


class TestDirections:

    def test_get_direction(self):
        directions = Directions('LLRR')

        assert directions.step() == Directions.instructions['L']
        assert directions.step() == Directions.instructions['L']
        assert directions.step() == Directions.instructions['R']
        assert directions.step() == Directions.instructions['R']
        assert directions.step() == Directions.instructions['L']
        assert directions.step() == Directions.instructions['L']

        directions = Directions('LR')
        assert directions.step() == Directions.instructions['L']
        assert directions.step() == Directions.instructions['R']
        assert directions.step() == Directions.instructions['L']
        assert directions.step() == Directions.instructions['R']
        assert directions.step() == Directions.instructions['L']


class TestDirectionsEnum:

    def test_directions_values(self):
        assert Directions.instructions['L'] == 0
        assert Directions.instructions['R'] == 1


class TestPart1:

    def test_answer(self):
        assert part1('day8/input_example') == 2
        assert part1() == 17287


class TestPart2:

    def test_answer(self):
        assert part2('day8/input_example_part2') == 6
        assert part2() == 18625484023687

    def test_python(self):
        assert 'AAZ'[-1] == 'Z'
