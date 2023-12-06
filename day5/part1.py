from collections import namedtuple


class Mapper():
    def __init__(self, source_category, destination_category) -> None:
        self.source_category = source_category
        self.destination_category = destination_category
        self.maps = []

    def add_map_entry(self, line):
        destination, source, length = map(int, line.strip().split())
        m = namedtuple('Map', ['destination', 'source', 'length'])
        self.maps.append(m(destination, source, length))

    def get_mapped_value(self, source):
        for m in self.maps:
            if m.source <= source <= (m.source + m.length):
                offset = source - m.source
                return m.destination + offset
        return source


def get_mapper(mappers, source_category) -> Mapper:
    result = next(
        (obj for obj in mappers if obj.source_category == source_category),
        None
    )
    return result


def main(filename):

    seeds = []
    mappers = []

    with open(filename, 'r') as file:
        currentMap = None
        for line in file:
            line = line.strip()
            if line.startswith('seeds:'):
                _, numbers = line.split(':')
                seeds = map(int, numbers.split())
            elif '-to-' in line:
                src_dst, _ = line.split()
                src, dst = src_dst.split('-to-')
                currentMap = Mapper(src, dst)
            elif '' == line:
                if currentMap is not None:
                    mappers.append(currentMap)
                    currentMap = None
            elif currentMap is not None:
                # maps for the current block
                currentMap.add_map_entry(line)
        mappers.append(currentMap)

    min_location = None
    for s in seeds:
        value = s
        src = 'seed'
        m = get_mapper(mappers, src)
        while m is not None:
            # print('{}:{}'.format(src, value))
            # print('  to   ')
            value = m.get_mapped_value(value)
            src = m.destination_category
            # print('{}:{}'.format(src, value))
            # print('------')
            m = get_mapper(mappers, src)

        if min_location is None:
            min_location = value
        elif min_location > value:
            min_location = value

        print('seed:{}, location:{}'.format(s, value))

    print(min_location)


if __name__ == "__main__":
    main('day5/input')
