import operator


def parse_line(line):
    return [int(x) for x in line.split()]


def all_zeros(readings):
    if not readings:
        return False
    return all([x == 0 for x in readings])


def differences(readings):
    return list(map(operator.sub, readings[1:], readings[:-1]))


def get_one_prediction(readings, diff, end=-1):
    if end == 0:
        return readings[end] - diff
    else:
        return readings[end] + diff


def predict(line, end=-1):
    root_readings = parse_line(line)
    diff_list = [root_readings]

    current_diff = []

    while not all_zeros(current_diff):
        current_diff = differences(diff_list[-1])
        diff_list.append(current_diff)

    current_diff = diff_list.pop()
    current_prediction = current_diff[end]
    while diff_list:
        current_prediction = get_one_prediction(
            current_diff, current_prediction, end)
        current_diff = diff_list.pop()

    if end == 0:
        return current_diff[end] - current_prediction
    else:
        return current_diff[end] + current_prediction


def part1(input='day9/input'):

    sum_predictions = 0

    with open(input) as file:
        for line in file:
            sum_predictions += predict(line)

    return sum_predictions


def part2(input='day9/input'):

    sum_predictions = 0

    with open(input) as file:
        for line in file:
            sum_predictions += predict(line, end=0)

    return sum_predictions


if __name__ == '__main__':
    print(part1())
    print(part2())
