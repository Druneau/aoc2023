import part1
import pytest


@pytest.fixture
def mapper():
    return part1.Mapper(source_category='seed', destination_category='soil')


class TestMapperClass:

    def test_map_init(self, mapper):
        assert mapper.source_category == 'seed'
        assert mapper.destination_category == 'soil'

    def test_map_add(self, mapper):
        mapper.add_map_entry('50 98 2')
        assert len(mapper.maps) == 1

    def test_mapped_value_no_map(self, mapper):
        assert mapper.get_mapped_value(1) == 1

    def test_mapped_value_one_map(self, mapper):
        mapper.add_map_entry('50 98 2')
        assert mapper.get_mapped_value(98) == 50
        assert mapper.get_mapped_value(99) == 51

    def test_mapped_value_two_maps(self, mapper):
        mapper.add_map_entry('50 98 2')
        mapper.add_map_entry('52 50 48')
        assert mapper.get_mapped_value(98) == 50
        assert mapper.get_mapped_value(99) == 51
        assert mapper.get_mapped_value(50) == 52
        assert mapper.get_mapped_value(97) == 99


@pytest.fixture
def mappers():
    ms = []
    ms.append(part1.Mapper(source_category='seed', destination_category='soil'))
    ms.append(part1.Mapper(source_category='soil',
              destination_category='fertilizer'))
    ms.append(part1.Mapper(source_category='fertilizer',
              destination_category='water'))
    ms.append(part1.Mapper(source_category='water',
              destination_category='light'))
    return ms


class TestMapperHelpers:

    def test_mapper_chain(self, mappers):
        assert part1.get_mapper(mappers, 'soil').source_category == 'soil'

    def test_mapper_none(self, mappers):
        assert part1.get_mapper(mappers, 'light') == None
