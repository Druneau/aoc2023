from day11 import (
    CosmicImage,
    part1,
    part2,
    load,
)

import pytest


class TestPart1:
    def test_part1(self):
        assert part1('day11/input_example', expansion_factor=1) == 292
        assert part1('day11/input_example', expansion_factor=2) == 374
        assert part1('day11/input_example', expansion_factor=10) == 1030
        assert part1('day11/input_example', expansion_factor=100) == 8410
        assert part1('day11/input', expansion_factor=2) == 10173804
        assert part1('day11/input', expansion_factor=10) == 15248332


class TestPart2:
    def test_part2(self):
        assert part2(expansion_factor=2) == 10173804
        assert part2(expansion_factor=1000000) == 10173804


class TestCosmicImageInit:
    def test_cosmic_image_init(self):
        image = load('day11/input_example')
        cosmic_image = CosmicImage(image, expansion_factor=2)
        assert cosmic_image.h_expand_indexes == [3, 7]
        assert cosmic_image.v_expand_indexes == [2, 5, 8]

        assert cosmic_image.image[2][0] == '#'
        assert cosmic_image.image[0][3] == '#'


class TestCosmicImageDistance:
    def test_number_expansions_between_galaxies(self):
        image = load('day11/input_simple')
        cosmic_image = CosmicImage(image)
        assert cosmic_image.get_number_expansions_between_galaxies(
            (0, 0), (2, 2)) == (1, 1)

        image = load('day11/input_example')
        cosmic_image = CosmicImage(image)
        assert cosmic_image.get_number_expansions_between_galaxies(
            (0, 3), (9, 0)) == (2, 1)
        assert cosmic_image.get_number_expansions_between_galaxies(
            (2, 0), (6, 9)) == (1, 3)
        assert cosmic_image.get_number_expansions_between_galaxies(
            (0, 3), (1, 7)) == (0, 1)

    def test_calc_distance_math_example(self):
        image = load('day11/input_example')
        cosmic_image = CosmicImage(image, expansion_factor=1)
        assert cosmic_image.calc_distance_math((3, 0), (7, 1)) == 5
        assert cosmic_image.calc_distance_math((3, 0), (0, 2)) == 5
        assert cosmic_image.calc_distance_math((3, 0), (6, 4)) == 7
        assert cosmic_image.calc_distance_math((3, 0), (1, 5)) == 7
        assert cosmic_image.calc_distance_math((3, 0), (9, 6)) == 12
        assert cosmic_image.calc_distance_math((3, 0), (7, 8)) == 12
        assert cosmic_image.calc_distance_math((3, 0), (0, 9)) == 12
        assert cosmic_image.calc_distance_math((3, 0), (4, 9)) == 10

        cosmic_image = CosmicImage(image, expansion_factor=2)
        assert cosmic_image.calc_distance_math((0, 3), (1, 7)) == 6

        cosmic_image.expansion_factor = 10
        assert cosmic_image.calc_distance_math((0, 3), (1, 7)) == 14
        assert cosmic_image.calc_distance_math((0, 3), (9, 4)) == 28
        assert cosmic_image.calc_distance_math((2, 0), (6, 9)) == 49

        cosmic_image.expansion_factor = 100
        assert cosmic_image.calc_distance_math((0, 3), (9, 4)) == 208
        assert cosmic_image.calc_distance_math((2, 0), (6, 9)) == 409

    def test_calc_sum_distance_math_simple(self):
        image = load('day11/input_simple')
        cosmic_image = CosmicImage(image, expansion_factor=1)
        assert cosmic_image.calc_sum_distances_math() == 4

        cosmic_image = CosmicImage(image, expansion_factor=2)
        assert cosmic_image.calc_sum_distances_math() == 6

        cosmic_image = CosmicImage(image, expansion_factor=10)
        assert cosmic_image.calc_sum_distances_math() == 22

        cosmic_image = CosmicImage(image, expansion_factor=100)
        assert cosmic_image.calc_sum_distances_math() == 202

    def test_calc_sum_distance_math_3_galaxies(self):
        image = load('day11/input_3_galaxies')
        cosmic_image = CosmicImage(image, expansion_factor=1)
        assert cosmic_image.calc_sum_distances_math() == 8

        cosmic_image = CosmicImage(image, expansion_factor=2)
        assert cosmic_image.calc_sum_distances_math() == 12

        cosmic_image = CosmicImage(image, expansion_factor=10)
        assert cosmic_image.calc_sum_distances_math() == 44

        cosmic_image = CosmicImage(image, expansion_factor=100)
        assert cosmic_image.calc_sum_distances_math() == 404

    def test_calc_sum_distance_math_example(self):
        image = load('day11/input_example')
        cosmic_image = CosmicImage(image, expansion_factor=1)
        assert cosmic_image.calc_sum_distances_math() == 292

        image = load('day11/input_example')
        cosmic_image = CosmicImage(image, expansion_factor=2)
        assert cosmic_image.calc_sum_distances_math() == 374


class TestCosmicImageTagging:
    def test_tag(self):
        image = [
            ['#', '.', '#'],
            ['.', '.', '.'],
            ['#', '.', '.'],
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.tag()
        assert cosmic_image.image == [
            ['1', '.', '2'],
            ['.', '.', '.'],
            ['3', '.', '.'],
        ]

    def test_calc_permutations(self):
        image = [
            ['#', '.', '#'],
            ['.', '.', '.'],
            ['#', '.', '.'],
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.tag()
        cosmic_image.calc_permutations()
        assert cosmic_image.permutations == [((1, (0, 0)), (2, (2, 0))), ((
            1, (0, 0)), (3, (0, 2))), ((2, (2, 0)), (3, (0, 2)))]

    def test_calc_sum_distances(self):
        image = [
            ['#', '.', '#'],
            ['.', '.', '.'],
            ['#', '.', '.'],
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.tag()
        cosmic_image.calc_permutations()
        assert cosmic_image.calc_sum_distances() == 8


class TestCosmicImageExpand:
    def test_can_expand(self):
        assert CosmicImage.can_expand(['.', '.', '.', '.']) == True
        assert CosmicImage.can_expand(['.', '#', '.', '.']) == False

    def test_extract_col(self):
        image = [
            ['.', '#', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        assert CosmicImage.extract_col(image, 0) == ['.', '.', '.']
        assert CosmicImage.extract_col(image, 1) == ['#', '.', '.']
        assert CosmicImage.extract_col(image, 2) == ['.', '.', '.']
        with pytest.raises(IndexError):
            assert CosmicImage.extract_col(image, -1)
            assert CosmicImage.extract_col(image, 3)

    def test_expand_col(self):
        image = [
            ['.', '#', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand_col(0)
        assert cosmic_image.image == [
            ['.', '.', '#', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]

        image = [
            ['.', '#', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand_col(2)
        assert cosmic_image.image == [
            ['.', '#', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]

    def test_create_cosmic_image(self):
        image = [
            ['.', '#', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        cosmic_image = CosmicImage(image)
        assert cosmic_image.image == image

    def test_expand_cosmic_image_rows(self):
        image = [
            ['.', '#', '.'],
            ['#', '.', '#'],
            ['.', '.', '.'],
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand()
        assert cosmic_image.image == [
            ['.', '#', '.'],
            ['#', '.', '#'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]

        image = [
            ['.', '#', '.'],
            ['.', '.', '.'],
            ['#', '.', '#'],
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand()
        assert cosmic_image.image == [
            ['.', '#', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['#', '.', '#']
        ]

    def test_expand_cosmic_image_cols(self):
        image = [
            ['.', '#', '.'],
            ['#', '.', '.'],
            ['.', '#', '.']
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand_cols()
        assert cosmic_image.image == [
            ['.', '#', '.', '.'],
            ['#', '.', '.', '.'],
            ['.', '#', '.', '.']
        ]

        image = [
            ['.', '#', '.'],
            ['.', '.', '#'],
            ['.', '#', '.']
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand_cols()
        assert cosmic_image.image == [
            ['.', '.', '#', '.'],
            ['.', '.', '.', '#'],
            ['.', '.', '#', '.']
        ]

        image = [
            ['#', '.', '.'],
            ['.', '.', '#'],
            ['#', '.', '.']
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand_cols()
        assert cosmic_image.image == [
            ['#', '.', '.', '.'],
            ['.', '.', '.', '#'],
            ['#', '.', '.', '.']
        ]

    def test_expand_cosmic_image_all(self):
        image = [
            ['#', '.', '.'],
            ['.', '#', '.'],
            ['.', '.', '#']
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand()
        assert cosmic_image.image == [
            ['#', '.', '.'],
            ['.', '#', '.'],
            ['.', '.', '#'],
        ]

        image = [
            ['#', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '#']
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand()
        assert cosmic_image.image == [
            ['#', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '#'],
        ]

        image = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '#']
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand()
        assert cosmic_image.image == [
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '#'],
        ]

        image = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        cosmic_image = CosmicImage(image)
        cosmic_image.expand()
        assert cosmic_image.image == [
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
        ]

    def test_expand_example(self):
        image = load('day11/input_example')
        image_expanded = load('day11/input_example_expanded')
        cosmic_image = CosmicImage(image)
        cosmic_image.expand()
        assert cosmic_image.image == image_expanded

    def test_get_expand_indexes(self):
        image = [
            ['.', '.', '.'],
            ['.', '#', '.'],
            ['.', '.', '.'],
        ]
        cosmic_image = CosmicImage(image)
        assert cosmic_image.get_expand_row_indexes() == [0, 2]
        assert cosmic_image.get_expand_col_indexes() == [0, 2]

    def test_get_expand_indexes(self):
        image = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        cosmic_image = CosmicImage(image)
        assert cosmic_image.get_expand_row_indexes() == [0, 1, 2]
        assert cosmic_image.get_expand_col_indexes() == [0, 1, 2]
