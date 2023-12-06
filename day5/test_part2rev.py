import part2rev as part2
import pytest


@pytest.fixture
def mapper() -> part2.Mapper:
    return part2.Mapper(source_category='seed', destination_category='soil')


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

    def test_unmapped_value_no_map(self, mapper):
        assert mapper.get_mapped_value(1) == 1

    def test_unmapped_value_one_map(self, mapper):
        mapper.add_map_entry('50 98 2')
        assert mapper.get_unmapped_value(50) == 98
        assert mapper.get_unmapped_value(51) == 99

    def test_unmapped_value_two_maps(self, mapper):
        mapper.add_map_entry('50 98 2')
        mapper.add_map_entry('52 50 48')
        assert mapper.get_unmapped_value(50) == 98
        assert mapper.get_unmapped_value(51) == 99
        assert mapper.get_unmapped_value(52) == 50
        assert mapper.get_unmapped_value(99) == 97


class TestRangeClass:

    def test_range_init(self):
        r = part2.Range(1, 10)
        assert r.start == 1
        assert r.end == 10

    def test_range_mapped(self, mapper):
        r = part2.Range(1, 10)
        mapper.add_map_entry('30 4 4')
        ranges = mapper.get_mapped_ranges(r)
        assert len(ranges) == 3

        assert ranges[0] == part2.Range(1, 3)
        assert ranges[1] == part2.Range(30, 33)
        assert ranges[2] == part2.Range(9, 10)
