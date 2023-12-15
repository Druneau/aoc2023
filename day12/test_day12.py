from day12 import Consume
from day12 import part1
from itertools import accumulate

import pytest


@pytest.fixture
def empty_return():
    return ('', [], 1)


def test_accumulate():
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]
    assert list(accumulate(accumulate([1, 2, 3, 4, 5]))) == [
        1, 4, 10, 20, 35]


def test_accumulate_level():
    assert list(Consume.accumulate_level(4, 2)) == [1, 3, 6, 10]
    assert list(Consume.accumulate_level(4, 3)) == [1, 4, 10, 20]
    assert list(Consume.accumulate_level(6, 4)) == [1, 5, 15, 35, 70, 126]
    assert list(Consume.accumulate_level(1, 10)) == [1]


def test_arrangements():
    assert Consume.arrangements(extra_space=0, spring_groups=1) == 1
    assert Consume.arrangements(extra_space=1, spring_groups=1) == 2
    assert Consume.arrangements(extra_space=2, spring_groups=1) == 3
    assert Consume.arrangements(extra_space=1, spring_groups=2) == 3
    assert Consume.arrangements(extra_space=2, spring_groups=2) == 6
    assert Consume.arrangements(extra_space=3, spring_groups=2) == 10
    assert Consume.arrangements(extra_space=10, spring_groups=1) == 11
    assert Consume.arrangements(extra_space=7, spring_groups=3) == 120
    assert Consume.arrangements(extra_space=8, spring_groups=4) == 495


class TestConsume:

    def test_consume_hashtag(self, empty_return):
        # from the LEFT
        assert Consume.hashtag('#.', [1]) == empty_return
        assert Consume.hashtag('#?', [1]) == empty_return
        assert Consume.hashtag('#???', [2, 1]) == ('?', [1], 1)
        assert Consume.hashtag('#???', [2, 1]) == ('?', [1], 1)
        assert Consume.hashtag('###????????', [3, 2, 1]) == (
            '???????', [2, 1], 1)

        # from the RIGHT
        assert Consume.hashtag('??#', [2]) == empty_return
        assert Consume.hashtag('?#', [1]) == empty_return
        assert Consume.hashtag('?##', [2]) == empty_return
        assert Consume.hashtag('???????#', [1, 2]) == ('?????', [1], 1)
        assert Consume.hashtag('??#????#', [1, 2]) == ('??#??', [1], 1)

        # from both ends...
        assert Consume.hashtag('#????#', [1, 2]) == empty_return
        assert Consume.hashtag('????', [1, 2]) == ('????', [1, 2], 1)
        assert Consume.hashtag('....', [], 100) == ('', [], 100)

    def test_consume_period(self, empty_return):
        assert Consume.period('.', [], 1) == empty_return
        assert Consume.period('.#.', [1]) == ('#', [1], 1)
        assert Consume.period('..#..', [1]) == ('#', [1], 1)
        assert Consume.period('...#.?.?..', [1, 1, 1]) == (
            '#.?.?', [1, 1, 1], 1)

        assert Consume.period('#', [1], 1) == ('#', [1], 1)
        assert Consume.period('#', [1], 2) == ('#', [1], 2)

    def test_consume_question(self, empty_return):
        assert Consume.question('?', [1]) == empty_return
        assert Consume.question('??', [1]) == ('', [], 2)
        assert Consume.question('???', [1]) == ('', [], 3)
        assert Consume.question('????', [1, 2]) == empty_return
        assert Consume.question('?????', [1, 2]) == ('', [], 3)

        assert Consume.question('?#?', [1]) == empty_return
        assert Consume.question('?##?', [2]) == empty_return

    def test_consume_loop(self, empty_return):
        assert Consume.recursive('.', [], 1) == empty_return
        assert Consume.recursive('.', [], 1) == empty_return
        assert Consume.recursive('#.', [1], 1) == empty_return
        assert Consume.recursive('????', [1], 1) == ('', [], 4)
        assert Consume.recursive('?###????????', [3, 2, 1], 1) == ('', [], 10)
        assert Consume.recursive('????.######..#####.', [
                                 1, 6, 5], 1) == ('', [], 4)
        assert Consume.recursive('?????...#??', [5, 1]) == ('', [], 1)
        assert Consume.recursive('???.???????', [1, 4]) == ('', [], 12)

        # assert Consume.recursive('.?#.#?#???.?#??', [2, 1, 2, 1, 3]) == 2

        assert Consume.recursive('#??.#.??????##?', [1, 1, 7]) == ('', [], 2)


def test_part1():
    pass
    # assert part1() == 1
