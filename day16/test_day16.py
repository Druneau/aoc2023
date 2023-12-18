import day16
from day16 import Elements
from day16 import UP, DOWN, LEFT, RIGHT
import pytest


@pytest.fixture
def contrap_empty():
    input = ['....', '....']
    return day16.Contraption(input)


@pytest.fixture
def contrap_example():
    input = [r'.|...\....',
             r'|.-.\.....',
             r'.....|-...',
             r'........|.',
             r'..........',
             r'.........\\',
             r'..../.\\..',
             r'.-.-/..|..',
             r'.|....-|.\\',
             r'..//.|....']
    return day16.Contraption(input)


class TestContraption:

    def test_contraption_init(self, contrap_empty, contrap_example):
        assert contrap_empty.width == 4
        assert contrap_empty.height == 2

        assert contrap_example.width == 10
        assert contrap_example.height == 10

    def test_contraption_usage(self, contrap_empty, contrap_example):
        assert contrap_empty.is_inside((0, 0)) == True
        assert contrap_empty.is_inside((3, 1)) == True
        assert contrap_empty.is_inside((3, 9)) == False

        assert contrap_example.is_inside((3, 9)) == True
        assert contrap_example.is_inside((10, 10)) == False

        assert contrap_empty.get_element((0, 0)) == Elements.EMPTY_SPACE
        assert contrap_example.get_element(
            (1, 0)) == Elements.SPLITTER_VERTICAL
        assert contrap_example.get_element((9, 8)) == Elements.MIRROR_BACKSLASH
        assert contrap_example.get_element(
            (6, 8)) == Elements.SPLITTER_HORIZONTAL

    def test_set_element_split(self, contrap_example):
        assert contrap_example.has_element_split((5, 2)) is False
        contrap_example.set_element_split((5, 2))
        assert contrap_example.has_element_split((5, 2)) is True

    def test_has_bounced_directional(self, contrap_example):
        assert contrap_example.has_bounced_directional((4, 1), LEFT) is False
        contrap_example.set_bounced_directional((4, 1), LEFT)
        assert contrap_example.has_bounced_directional((4, 1), LEFT) is True
        assert contrap_example.has_bounced_directional((4, 1), UP) is False


class TestBeam():

    @pytest.fixture
    def beam_empty(self, contrap_empty):
        return day16.Beam(contrap_empty, -1, 0, RIGHT)

    @pytest.fixture
    def beam_example(self, contrap_example):
        return day16.Beam(contrap_example, -1, 0, RIGHT)

    def test_bounce(self):
        assert day16.Beam.bounce(Elements.MIRROR_SLASH, UP) == RIGHT
        assert day16.Beam.bounce(Elements.MIRROR_SLASH, DOWN) == LEFT
        assert day16.Beam.bounce(Elements.MIRROR_SLASH, LEFT) == DOWN
        assert day16.Beam.bounce(Elements.MIRROR_SLASH, RIGHT) == UP

        assert day16.Beam.bounce(Elements.MIRROR_BACKSLASH, UP) == LEFT
        assert day16.Beam.bounce(Elements.MIRROR_BACKSLASH, DOWN) == RIGHT
        assert day16.Beam.bounce(Elements.MIRROR_BACKSLASH, LEFT) == UP
        assert day16.Beam.bounce(Elements.MIRROR_BACKSLASH, RIGHT) == DOWN

        assert day16.Beam.bounce(Elements.EMPTY_SPACE, UP) == None
        assert day16.Beam.bounce(Elements.SPLITTER_HORIZONTAL, UP) == None
        assert day16.Beam.bounce(Elements.SPLITTER_VERTICAL, UP) == None

    def test_beam_init(self, contrap_empty):
        beam = day16.Beam(contrap_empty, -1, 0, RIGHT)
        assert beam.x == -1
        assert beam.y == 0
        assert beam.direction == RIGHT

        beam_split = day16.Beam(contrap_empty, 1, 1, DOWN)
        assert beam_split.x == 1
        assert beam_split.y == 1
        assert beam_split.location == (1, 1)
        assert beam_split.direction == DOWN

    def test_beam_step_empty(self, beam_empty):
        beam_empty.step()
        assert beam_empty.location == (0, 0)
        beam_empty.step()
        assert beam_empty.location == (1, 0)
        beam_empty.step()
        assert beam_empty.location == (2, 0)
        assert beam_empty.is_alive is True

    def test_beam_step_into_spillter_vertical(self, beam_example):
        beam_example.step()
        assert beam_example.element == Elements.EMPTY_SPACE

        beam_up, beam_down = beam_example.step()
        assert beam_example.element == Elements.SPLITTER_VERTICAL
        assert beam_example.is_alive == False

        assert beam_up.element == Elements.SPLITTER_VERTICAL
        assert beam_up.location == (1, 0)
        beam_up.step()
        assert beam_up.location == None
        assert beam_up.is_alive is False

        assert beam_down.element == Elements.SPLITTER_VERTICAL
        assert beam_down.location == (1, 0)
        beam_down.step()
        assert beam_down.location == (1, 1)
        assert beam_down.is_alive is True

    def test_beam_step_into_splitter_horizontal(self, beam_example):
        beam_example.x = 1
        beam_example.y = 6
        beam_example.direction = DOWN
        assert beam_example.element == Elements.EMPTY_SPACE
        beam_left, beam_right = beam_example.step()
        assert beam_example.element == Elements.SPLITTER_HORIZONTAL
        assert beam_example.location == (1, 7)

        beam_left.step()
        assert beam_left.location == (0, 7)
        beam_left.step()
        assert beam_left.is_alive is False

        beam_right.step()
        assert beam_right.location == (2, 7)
        beam_right.step()
        assert beam_right.element == Elements.SPLITTER_HORIZONTAL
        beam_right.step()
        assert beam_right.is_alive is True

    def test_beam_step_into_mirror_slash(self, beam_example):
        beam_example.x = 3
        beam_example.y = 6
        ret_value = beam_example.step()
        assert ret_value is None
        assert beam_example.direction == UP


def test_part1():
    assert day16.part1('day16/input_example.txt') == 46
    assert day16.part1() == 8146
