from Direction import Direction
from day10 import (
    get_pipe_exit,
    get_possible_exit_directions,
    part1,
    load,
    get_start_location,
    move,
    get_symbol_if_exists,
    can_enter_pipe,
    reverse_direction,
    part2
)

import pytest


class TestDirection:

    def test_get_pipe_exit(self):
        assert get_pipe_exit('|', entry=Direction.NORTH) == Direction.SOUTH
        assert get_pipe_exit('|', entry=Direction.SOUTH) == Direction.NORTH

        assert get_pipe_exit('-', entry=Direction.WEST) == Direction.EAST
        assert get_pipe_exit('-', entry=Direction.EAST) == Direction.WEST

        assert get_pipe_exit('L', entry=Direction.NORTH) == Direction.EAST
        assert get_pipe_exit('L', entry=Direction.EAST) == Direction.NORTH

        assert get_pipe_exit('J', entry=Direction.WEST) == Direction.NORTH
        assert get_pipe_exit('J', entry=Direction.NORTH) == Direction.WEST

        assert get_pipe_exit('7', entry=Direction.WEST) == Direction.SOUTH
        assert get_pipe_exit('7', entry=Direction.SOUTH) == Direction.WEST

        assert get_pipe_exit('F', entry=Direction.SOUTH) == Direction.EAST
        assert get_pipe_exit('F', entry=Direction.EAST) == Direction.SOUTH

        assert get_pipe_exit('.', entry=Direction.WEST) == Direction.NONE

        assert get_pipe_exit('S', entry=Direction.EAST) == Direction.NONE

    def test_can_enter_pipe(self):
        assert can_enter_pipe('|', Direction.NORTH) == True
        assert can_enter_pipe('|', Direction.EAST) == False
        assert can_enter_pipe('|', Direction.SOUTH) == True
        assert can_enter_pipe('|', Direction.WEST) == False

        assert can_enter_pipe('-', Direction.NORTH) == False
        assert can_enter_pipe('-', Direction.EAST) == True
        assert can_enter_pipe('-', Direction.SOUTH) == False
        assert can_enter_pipe('-', Direction.WEST) == True

        assert can_enter_pipe('J', Direction.NORTH) == False
        assert can_enter_pipe('J', Direction.EAST) == True
        assert can_enter_pipe('J', Direction.SOUTH) == True
        assert can_enter_pipe('J', Direction.WEST) == False

        assert can_enter_pipe('7', Direction.NORTH) == True
        assert can_enter_pipe('7', Direction.EAST) == True
        assert can_enter_pipe('7', Direction.SOUTH) == False
        assert can_enter_pipe('7', Direction.WEST) == False

        assert can_enter_pipe('F', Direction.NORTH) == True
        assert can_enter_pipe('F', Direction.EAST) == False
        assert can_enter_pipe('F', Direction.SOUTH) == False
        assert can_enter_pipe('F', Direction.WEST) == True

        assert can_enter_pipe('.', Direction.NORTH) == False
        assert can_enter_pipe('.', Direction.EAST) == False
        assert can_enter_pipe('.', Direction.SOUTH) == False
        assert can_enter_pipe('.', Direction.WEST) == False

    def test_direction_enum(self):
        assert Direction.NORTH != Direction.EAST
        assert Direction.SOUTH != Direction.WEST
        assert Direction.NORTH.value == (-1, 0)
        assert 1 == (1, 0)[0]


class TestSearch:

    def test_search_exit_north(self):

        assert get_possible_exit_directions([(Direction.NORTH, '|')]) == [
            Direction.NORTH]
        assert get_possible_exit_directions([(Direction.NORTH, '7')]) == [
            Direction.NORTH]
        assert get_possible_exit_directions([(Direction.NORTH, 'F')]) == [
            Direction.NORTH]

        assert get_possible_exit_directions([(Direction.EAST, '7')]) == [
            Direction.EAST]

    def test_search_exit_east(self):

        assert get_possible_exit_directions([(Direction.EAST, 'J')]) == [
            Direction.EAST]
        assert get_possible_exit_directions([(Direction.EAST, '-')]) == [
            Direction.EAST]
        assert get_possible_exit_directions([(Direction.EAST, '7')]) == [
            Direction.EAST]

    def test_search_exit_south(self):
        possible_pipe_shapes = []
        possible_pipe_shapes.append((Direction.NORTH, '-'))
        possible_pipe_shapes.append((Direction.EAST, '|'))
        possible_pipe_shapes.append((Direction.SOUTH, '|'))
        possible_pipe_shapes.append((Direction.WEST, '|'))

        assert get_possible_exit_directions(possible_pipe_shapes) == [
            Direction.SOUTH]

    def test_search_exit_west(self):
        possible_pipe_shapes = []
        possible_pipe_shapes.append((Direction.NORTH, '-'))
        possible_pipe_shapes.append((Direction.EAST, '|'))
        possible_pipe_shapes.append((Direction.SOUTH, '-'))
        possible_pipe_shapes.append((Direction.WEST, '-'))

        assert get_possible_exit_directions(possible_pipe_shapes) == [
            Direction.WEST]

    def test_search_exit_east_south(self):
        possible_pipe_shapes = []
        possible_pipe_shapes.append((Direction.NORTH, '.'))
        possible_pipe_shapes.append((Direction.EAST, 'J'))
        possible_pipe_shapes.append((Direction.SOUTH, '|'))
        possible_pipe_shapes.append((Direction.WEST, '.'))

        assert set([Direction.EAST, Direction.SOUTH]) == set(
            [Direction.SOUTH, Direction.EAST])

        assert set(get_possible_exit_directions(possible_pipe_shapes)) == set([
            Direction.EAST, Direction.SOUTH])


class TestPart1:
    def test_part1(self):
        assert part1('day10/input_example') == 8
        assert part1() == 6690


class TestPart2:
    def test_part2(self):
        assert part2() == 1


def test_get_start():
    assert get_start_location(
        _map=load('day10/input_example'), symbol='S') == (2, 0)


def test_reverse_direction():
    assert reverse_direction(Direction.NORTH) == Direction.SOUTH
    assert reverse_direction(Direction.SOUTH) == Direction.NORTH
    assert reverse_direction(Direction.WEST) == Direction.EAST
    assert reverse_direction(Direction.EAST) == Direction.WEST


def test_move():
    assert move((0, 0), Direction.NORTH) == (-1, 0)
    assert move((0, 0), Direction.EAST) == (0, 1)
    assert move((0, 0), Direction.SOUTH) == (1, 0)
    assert move((0, 0), Direction.WEST) == (0, -1)


def test_symbol_if_exists():
    _map = load('day10/input_example')
    assert get_symbol_if_exists(_map, (-1, -1)) == '.'
    assert get_symbol_if_exists(_map, (0, 0)) == '7'
    assert get_symbol_if_exists(_map, (0, 4)) == '-'
    assert get_symbol_if_exists(_map, (4, 0)) == 'L'
    assert get_symbol_if_exists(_map, (4, 4)) == 'J'
    assert get_symbol_if_exists(_map, (5, 5)) == '.'


class TestPython:
    def test_char_index(self):
        assert 'aaZaaaaaa'.index('Z') == 2
        with pytest.raises(ValueError):
            assert 'aaaZaaaa'.index('A')
