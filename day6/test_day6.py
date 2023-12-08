import part1

import pytest


@pytest.fixture
def race():
    return part1.Race(time=7, record=9)


class TestRace:
    def test_short_race(self, race):
        assert race.calc_distance(0) == 0

    def test_mid_race(self, race):
        assert race.calc_distance(4) == 12

    def test_max_race(self, race):
        assert race.calc_distance(race.time) == 0

    def test_wins(self, race):
        assert race.get_wins_count() == 4
