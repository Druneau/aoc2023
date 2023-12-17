import day15


def test_hash():
    assert day15.hash('HASH') == 52
    assert day15.hash('rn=1') == 30
    assert day15.hash('cm-') == 253
    assert day15.hash('qp=3') == 97
    assert day15.hash('cm=2') == 47
    assert day15.hash('qp-') == 14
    assert day15.hash('pc=4') == 180
    assert day15.hash('ot=9') == 9
    assert day15.hash('ab=5') == 197
    assert day15.hash('pc-') == 48
    assert day15.hash('pc=6') == 214
    assert day15.hash('ot=7') == 231


def test_parse_and_hash():
    assert day15.parse_and_hash('rn=1') == ('rn', '=', 1, 0)
    assert day15.parse_and_hash('cm-') == ('cm', '-', None, 0)
    assert day15.parse_and_hash('qp=3') == ('qp', '=', 3, 1)
    assert day15.parse_and_hash('cm=2') == ('cm', '=', 2, 0)


def test_get_lens_index():
    assert day15.get_lens_index(['rn 1', 'qp 3', 'cm 2'], 'rn') == 0
    assert day15.get_lens_index(['rn 1', 'qp 3', 'cm 2'], 'cm') == 2
    assert day15.get_lens_index(['rn 1', 'qp 3', 'cm 2'], 'zz') == None


def test_update_lens():
    assert day15.update_lens(['rn 1', 'qp 3'], 'rn', 3) == ['rn 3', 'qp 3']
    assert day15.update_lens(['rn 1', 'qp 3'], 'cm', 9) == [
        'rn 1', 'qp 3', 'cm 9']


def test_remove_lens():
    assert day15.remove_lens(['rn 1', 'qp 3'], 'rn') == ['qp 3']
    assert day15.remove_lens(['rn 1', 'qp 3'], 'qp') == ['rn 1']


def test_part1():
    assert day15.part1(input='day15/input_example.txt') == 1320
    assert day15.part1() == 514025


def test_part2():
    assert day15.part2(input='day15/input_example.txt') == 145
    assert day15.part2() == 244461
