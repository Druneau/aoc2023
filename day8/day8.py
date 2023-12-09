import math


class Directions:
    instructions = {'L': 0, 'R': 1}

    def __init__(self, directions) -> None:
        self.steps = 0
        self.directions = directions
        self.directions_count = len(directions)

    def step(self):
        self.steps += 1
        steps_as_index = self.steps % self.directions_count - 1
        current_instruction = self.directions[steps_as_index]

        return Directions.instructions[current_instruction]


def parse_node(line):
    node_from, node_to = line.split(' = (')

    # drop trailling )
    node_to = node_to[0:-1]

    node_to_left, node_to_right = node_to.split(', ')

    dict_node = {node_from: (node_to_left, node_to_right)}
    return dict_node


def parse_file(path):
    nodes = {}
    directions = None
    with open(path) as file:
        for line in file:
            line = line.strip()

            if directions is None:
                directions = Directions(line)
            elif line != '':
                new_node = parse_node(line)
                nodes.update(new_node)

    return nodes, directions


def part1(input='day8/input'):
    node_start = 'AAA'
    node_end = 'ZZZ'

    nodes, directions = parse_file(input)

    while node_start != node_end:
        current_node = nodes[node_start]
        node_start = current_node[directions.step()]

    return directions.steps


def part2(input='day8/input'):

    nodes, directions = parse_file(input)

    nodes_start = [k for k in nodes.keys() if 'A' == k[-1]]

    steps = []

    for node in nodes_start:
        node_start = node
        directions.steps = 0
        while node_start[-1] != 'Z':
            current_node = nodes[node_start]
            node_start = current_node[directions.step()]
        steps.append(directions.steps)

    # Brute force
    # while not all(last == 'Z' for (_, _, last) in nodes_start):

    #    current_nodes = [nodes[k] for k in nodes_start]
    #    step_direction = directions.step()
    #    nodes_start = [v[step_direction] for v in current_nodes]
    #    print(nodes_start)

    return math.lcm(*steps)


if __name__ == '__main__':
    print(part1())
    print(part2())
