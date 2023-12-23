import operator
from typing import Dict, List


class Part():
    def __init__(self, part_string) -> None:
        part_string = part_string[1:-1]
        key_value_pairs = part_string.split(',')

        self.values: Dict[str, int] = {}
        for kvp in key_value_pairs:
            key, value = kvp.split('=')
            self.values[key] = int(value)


class Workflow():
    def __init__(self, workflow_string) -> None:
        self.name, _ = workflow_string.split('{')
        self.rules = Workflow.parse_rules(workflow_string)

    def match(self, part) -> str:
        for rule in self.rules:
            if rule.input is None:
                return rule.output
            if rule.input in part.values:
                if rule.compare(part.values[rule.input]):
                    return rule.output

    @staticmethod
    def parse_rules(workflow_string: str) -> List['Rule']:
        workflow_string = workflow_string[:-1]
        _, rules = workflow_string.split('{')

        rules = rules.split(',')

        return [Rule(s) for s in rules]


class Rule():
    def __init__(self, rule_string: str) -> None:
        self.input, self.operator, self.value, self.output = self.parse_rule(
            rule_string)

    def parse_rule(self, rule_string):
        if ':' in rule_string:
            input = rule_string[0]
            operator = Rule.get_operator_function(rule_string[1])
            value = int(rule_string[2:].split(':')[0])
            output = rule_string.split(':')[1]
        else:
            input = operator = value = None
            output = rule_string

        return input, operator, value, output

    def compare(self, part_value):
        return self.operator(part_value, self.value)

    @staticmethod
    def get_operator_function(operator_symbol):
        if operator_symbol == '>':
            return operator.gt
        elif operator_symbol == '<':
            return operator.lt


def read_until_empty_line(file):
    for line in file:
        stripped_line = line.strip()
        if stripped_line:
            yield stripped_line
        else:
            break


def part1(input='day19/input.txt'):
    workflows = []

    with open(input, 'r') as file:
        workflows = {Workflow(line).name: Workflow(line)
                     for line in read_until_empty_line(file)}
        parts = [Part(l.strip()) for l in read_until_empty_line(file)]

        sum_accepted = 0

        for part in parts:
            workflow = workflows['in']
            output = None
            while output not in ['A', 'R']:
                output = workflow.match(part)
                if output == 'A' or output == 'R':
                    break
                workflow = workflows[output]
            if output == 'A':
                sum_accepted += sum(part.values.values())

        return sum_accepted
