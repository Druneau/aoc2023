import day19
import pytest
import operator


@pytest.fixture
def workflow():
    return day19.Workflow('px{a<2006:qkq,m>2090:A,rfg}')


@pytest.fixture
def part():
    return day19.Part('{x=787,m=2655,a=1222,s=2876}')


def test_rule_init():
    rule = day19.Rule('a<2:qkq')
    assert rule.input == 'a'
    assert rule.operator == operator.lt
    assert rule.value == 2
    assert rule.output == 'qkq'

    rule = day19.Rule('x>9999:A')
    assert rule.input == 'x'
    assert rule.operator == operator.gt
    assert rule.value == 9999
    assert rule.output == 'A'

    rule = day19.Rule('rfg')
    assert rule.input is None
    assert rule.operator is None
    assert rule.value is None
    assert rule.output == 'rfg'

    rule = day19.Rule('A')
    assert rule.input is None
    assert rule.operator is None
    assert rule.value is None
    assert rule.output == 'A'


def test_workflow_init(workflow, part):

    assert workflow.name == 'px'

    assert len(workflow.rules) == 3

    assert workflow.match(part) == 'qkq'


def test_part_init(part):

    assert part.values['x'] == 787
    assert part.values['m'] == 2655
    assert part.values['a'] == 1222
    assert part.values['s'] == 2876


def test_part1():
    assert day19.part1(input='day19/input_example.txt') == 19114
    assert day19.part1() == 367602
