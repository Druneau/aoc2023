from day11 import (
    CosmicImage,
    part1,
    load,
    print_array
)

import pytest


class TestPart1:
    def test_part1(self):
        assert part1('day11/input_example') == 374
        assert part1('day11/input') == 10173804


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
