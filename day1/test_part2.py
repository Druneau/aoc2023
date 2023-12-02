from part2 import getCalibrationValue


def test_digits():
    assert getCalibrationValue('111122222') == 12


def test_chars():
    assert getCalibrationValue('pqr3stu8vwx') == 38


def test_single_digit():
    assert getCalibrationValue('asdf6asdf') == 66


def test_word():
    assert getCalibrationValue('aonesdfasdf') == 11


def test_shared_letter():
    assert getCalibrationValue('oneight') == 18
