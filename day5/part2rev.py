from collections import namedtuple


class Mapper():
    def __init__(self, source_category, destination_category) -> None:
        self.source_category = source_category
        self.destination_category = destination_category
        self.maps = []

    def add_map_entry(self, line):
        destination, source, length = map(int, line.strip().split())
        source_range = Range(source, source + length)
        destination_range = Range(destination, destination + length)

        m = namedtuple('Map', ['destination', 'source', 'length'])
        self.maps.append(m(destination, source, length))

    def get_mapped_value(self, source):
        for m in self.maps:
            if m.source <= source <= (m.source + m.length):
                offset = source - m.source
                return m.destination + offset
        return source

    def get_unmapped_value(self, destination):
        for m in self.maps:
            if m.destination <= destination <= (m.destination + m.length - 1):
                offset = destination - m.destination
                return m.source + offset
        return destination

    def get_mapped_ranges(self, range):
        raise NotImplementedError


class Range:

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def split_at(self, index):
        raise NotImplementedError

    def in_range(self, number):
        return self.start <= number <= self.end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def get_mapper(mappers, source_category) -> Mapper:
    result = next(
        (obj for obj in mappers if obj.source_category == source_category),
        None
    )
    return result


def get_seeds_range(start, length):
    return Range(start=start, end=start+length)


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

    # trying to speedup computation...
    mappers_dict = {}
    for m in mappers:
        mappers_dict[m.source_category] = m

    # trying harder....!
    m_seed = get_mapper(mappers, 'seed')
    m_soil = get_mapper(mappers, 'soil')
    m_fertilizer = get_mapper(mappers, 'fertilizer')
    m_water = get_mapper(mappers, 'water')
    m_light = get_mapper(mappers, 'light')
    m_temperature = get_mapper(mappers, 'temperature')
    m_humidity = get_mapper(mappers, 'humidity')
    m_location = get_mapper(mappers, 'location')

    min_location = None

    seed_ranges = []
    seeds = iter(seeds)
    for seed_start in seeds:
        length = next(seeds)
        seed_ranges.append(Range(seed_start, seed_start + length))

    location_guess = 50000000
    found = False

    print('first guess: {}'.format(location_guess))
    while not found:

        if location_guess % 10000 == 0:
            print("\r>> Tried {} locations...".format(
                location_guess), end='')
        value = location_guess
        value = m_humidity.get_unmapped_value(value)
        value = m_temperature.get_unmapped_value(value)
        value = m_light.get_unmapped_value(value)
        value = m_water.get_unmapped_value(value)
        value = m_fertilizer.get_unmapped_value(value)
        value = m_soil.get_unmapped_value(value)
        value = m_seed.get_unmapped_value(value)

        for seed_range in seed_ranges:
            if seed_range.in_range(value):
                found = True
                print('')
                print('seed:{}, location:{}'.format(value, location_guess))
                break

        location_guess += 1


if __name__ == "__main__":
    main('day5/input')
