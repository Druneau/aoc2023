from typing import List, Tuple, Optional


def hash(lens_info: str) -> int:
    cur_value = 0

    for c in lens_info:
        cur_value += ord(c)
        cur_value *= 17
        cur_value %= 256

    return cur_value


def parse_and_hash(step: str) -> Tuple[str, str, int, int]:
    if '-' in step:
        lens, action, focal = (step[:-1], step[-1], None)
    else:
        lens, action, focal = (step[:-2], step[-2], int(step[-1]))

    lens_hash = hash(lens)

    return (lens, action, focal, lens_hash)


def load_init_sequence(input: str) -> List[str]:
    init_sequence = []

    with open(input, 'r') as file:
        for line in file:
            line = line.strip()
            init_sequence = line.split(',')
    return init_sequence


def get_lens_index(box: List[str], lens: str) -> Optional[int]:
    try:
        return next(i for i, v in enumerate(box) if v.startswith(lens))
    except StopIteration:
        return None


def remove_lens(box: List[str], lens: str) -> List[str]:
    index = get_lens_index(box, lens)
    if index is not None:
        del box[index]
    return box


def update_lens(box: List[str], lens: str, focal: int) -> List[str]:

    index = get_lens_index(box, lens)
    label = lens + ' ' + str(focal)

    if index is None:
        box.append(label)
    else:
        box[index] = label

    return box


def part1(input: str = 'day15/input.txt') -> int:
    sum_hashes = 0

    for seq in load_init_sequence(input):
        sum_hashes += hash(seq)

    return sum_hashes


def focusing_power(hash: int, index: int, focal: int) -> int:
    return (hash+1)*index*focal


def part2(input: str = 'day15/input.txt') -> int:

    boxes = {}

    for seq in load_init_sequence(input):
        lens, action, focal, hash = parse_and_hash(seq)

        box = boxes.get(hash, [])

        if action == '=':
            boxes[hash] = update_lens(box, lens, focal)
        elif action == '-':
            box = remove_lens(box, lens)

        boxes[hash] = box

    total_focusing_power = 0
    for hash, lenses in boxes.items():
        for i, lens in enumerate(lenses, start=1):
            _, focal = lens.split()
            focal = int(focal)
            total_focusing_power += focusing_power(hash, i, focal)

    return total_focusing_power


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
