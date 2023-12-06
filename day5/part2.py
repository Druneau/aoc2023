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

    def get_mapped_ranges(self, range):
        raise NotImplementedError


class Range:

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def split_at(self, index):
        raise NotImplementedError

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def get_mapper(mappers, source_category) -> Mapper:
    result = next(
        (obj for obj in mappers if obj.source_category == source_category),
        None
    )
    return result


def get_seeds_range(start, length):
    return range(start, start+length)


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

    seeds = iter(seeds)
    for sr in seeds:
        length = next(seeds)
        final_seed = sr + length
        seed_range = range(sr, sr+length)

        for s in seed_range:

            if s % 100000 == 0:
                print("\r>> starting seed {} of {}".format(
                    s-sr, length,), end='')
            value = s
            src = 'seed'
            value = m_seed.get_mapped_value(value)
            value = m_soil.get_mapped_value(value)
            value = m_fertilizer.get_mapped_value(value)
            value = m_water.get_mapped_value(value)
            value = m_light.get_mapped_value(value)
            value = m_temperature.get_mapped_value(value)
            value = m_humidity.get_mapped_value(value)

            if min_location is None:
                min_location = value
            elif min_location > value:
                min_location = value

        print('-----------------------')

    print(min_location)


if __name__ == "__main__":
    main('day5/input')
