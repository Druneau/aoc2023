from day9 import differences, parse_line, get_one_prediction, all_zeros, part1, predict, part2


def test_diff_steps():
    assert differences([0, 3, 6, 9, 12, 15]) == [3, 3, 3, 3, 3]
    assert differences([3, 3, 3, 3, 3]) == [0, 0, 0, 0]


def test_parse_line():
    assert parse_line('0 3 6 9 12 15') == [0, 3, 6, 9, 12, 15]


def test_prediction():
    assert get_one_prediction([3, 3, 3, 3, 3], 0) == 3
    assert get_one_prediction([0, 3, 6, 9, 12, 15], 3) == 18
    assert get_one_prediction([0, 3, 6, 9, 12, 15], 3, end=0) == -3


def test_predict():
    assert predict('0 3 6 9 12 15') == 18
    assert predict('10 13 16 21 30 45') == 68

    assert predict('0 3 6 9 12 15', end=0) == -3
    assert predict('10  13  16  21  30  45', end=0) == 5


def test_all_zero():
    assert all_zeros([]) == False
    assert all_zeros([0, 0, 0]) == True
    assert all_zeros([0, 0, 1]) == False


def test_list_pop():
    list = [1, 2, 3]
    last = list.pop()
    assert list == [1, 2]
    assert last == 3


class TestPart1:
    def test_part1(self):
        assert part1('day9/input_example') == 114
        assert part1() == 1684566095


class TestPart2:
    def test_part2(self):
        assert part2('day9/input_example') == 2
        assert part2() == 1136
