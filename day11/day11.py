from itertools import combinations


class CosmicImage:
    def __init__(self, image, expansion_factor=2):
        self.image = image
        self.expansion_factor = expansion_factor
        self.h_expand_indexes = self.get_expand_row_indexes()
        self.c_expand_indexes = self.get_expand_col_indexes()
        self.find_galaxies()
        self.calc_permutations()

    def find_galaxies(self):
        galaxy_locations = []
        row_number = 0
        for row in self.image:
            for i in range(len(row)):
                if row[i] == '#':
                    galaxy_locations.append((row_number, i))
            row_number += 1
        self.galaxies = galaxy_locations

    def tag(self):
        galaxy_locations = []
        galaxy_count = 0
        for row in self.image:
            for i in range(len(row)):
                if row[i] == '#':
                    galaxy_count += 1
                    row[i] = str(galaxy_count)
                    galaxy_locations.append(
                        (galaxy_count, (i, self.image.index(row))))
        self.galaxies = galaxy_locations

    def calc_permutations(self):
        self.permutations = list(combinations(self.galaxies, 2))

    def calc_sum_distances(self):
        sum_distance = 0
        for permutation in self.permutations:
            galaxy1, galaxy2 = permutation
            sum_distance += self.calc_distance(galaxy1, galaxy2)

        return sum_distance

    def calc_sum_distances_math(self):
        sum_distance = 0
        for permutation in self.permutations:
            galaxy1, galaxy2 = permutation
            sum_distance += self.calc_distance_math(galaxy1, galaxy2)

        return sum_distance

    def calc_distance(self, galaxy1, galaxy2):
        _, galaxy1_location = galaxy1
        _, galaxy2_location = galaxy2
        galaxy1_x, galaxy1_y = galaxy1_location
        galaxy2_x, galaxy2_y = galaxy2_location
        distance = abs(galaxy1_x - galaxy2_x) + abs(galaxy1_y - galaxy2_y)
        return distance

    def calc_distance_math(self, galaxy1, galaxy2):
        galaxy1_r, galaxy1_c = galaxy1
        galaxy2_r, galaxy2_c = galaxy2

        r_n, c_n = self.get_number_expansions_between_galaxies(
            galaxy1, galaxy2)

        factor = max(0, self.expansion_factor - 1)

        r_distance = abs(galaxy1_r - galaxy2_r)
        c_distance = abs(galaxy1_c - galaxy2_c)

        r_distance += r_n * factor
        c_distance += c_n * factor

        distance = r_distance + c_distance

        # print('r:{}->{} n={};c:{}->{} n={}; d={}'.format(galaxy1_r,
        #      galaxy2_r, r_n, galaxy1_c, galaxy2_c, c_n, distance))
        return distance

    def get_number_expansions_between_galaxies(self, galaxy1, galaxy2):
        galaxy1_r, galaxy1_c = galaxy1
        galaxy2_r, galaxy2_c = galaxy2

        r_n = 0

        low_r = min(galaxy1_r, galaxy2_r)
        high_r = max(galaxy1_r, galaxy2_r)
        for i in self.h_expand_indexes:
            if low_r < i < high_r:
                r_n += 1

        c_n = 0

        low_c = min(galaxy1_c, galaxy2_c)
        high_c = max(galaxy1_c, galaxy2_c)
        for i in self.v_expand_indexes:
            if low_c < i < high_c:
                c_n += 1

        return r_n, c_n

    def expand(self):
        self.expand_cols()
        self.expand_rows()

    def expand_rows(self):
        rows_to_expand = []
        for i in range(len(self.image)):
            row = self.image[i]
            if self.can_expand(row):
                for _ in range(self.expansion_factor - 1):
                    rows_to_expand.append(i)

        self.expand_rows = rows_to_expand

        for row_index in reversed(rows_to_expand):
            self.expand_row(row_index)

    def get_expand_row_indexes(self):
        rows_to_expand = []
        for i in range(len(self.image)):
            row = self.image[i]
            if self.can_expand(row):
                rows_to_expand.append(i)

        self.h_expand_indexes = rows_to_expand
        return rows_to_expand

    def expand_row(self, row_index):
        row = self.image[row_index]
        self.image.insert(row_index, row)

    def expand_cols(self):
        cols_to_expand = []
        for i in range(len(self.image[0])):
            col = self.extract_col(self.image, i)
            if self.can_expand(col):
                for _ in range(self.expansion_factor - 1):
                    cols_to_expand.append(i)

        self.expand_cols = cols_to_expand

        for col_index in reversed(cols_to_expand):
            self.expand_col(col_index)

    def expand_col(self, col_index):
        for row in self.image:
            row.insert(col_index, '.')

    def get_expand_col_indexes(self):
        cols_to_expand = []
        for i in range(len(self.image[0])):
            col = self.extract_col(self.image, i)
            if self.can_expand(col):
                cols_to_expand.append(i)

        self.v_expand_indexes = cols_to_expand
        return cols_to_expand

    @staticmethod
    def can_expand(array):
        return array.count('#') == 0

    @staticmethod
    def extract_col(image, col_index):
        return [row[col_index] for row in image]


def load(input):
    with open(input) as file:
        image = [list(line.strip()) for line in file]
    return image


def part1(input='day11/input', expansion_factor=2):
    image = load(input)
    cosmic_image = CosmicImage(image, expansion_factor)
    cosmic_image.expand()
    cosmic_image.tag()
    cosmic_image.calc_permutations()
    return cosmic_image.calc_sum_distances()


def part2(input='day11/input', expansion_factor=2):
    image = load(input)
    cosmic_image = CosmicImage(image, expansion_factor=expansion_factor)
    cosmic_image.calc_permutations()
    return cosmic_image.calc_sum_distances_math()


def print_array(loop):
    print('')
    for row in loop:
        for i in row:
            print(i, end='')
        print('')


if __name__ == '__main__':
    print(part1())
