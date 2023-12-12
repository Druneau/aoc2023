from itertools import combinations


class CosmicImage:
    def __init__(self, image):
        self.image = image

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

    def calc_distance(self, galaxy1, galaxy2):
        _, galaxy1_location = galaxy1
        _, galaxy2_location = galaxy2
        galaxy1_x, galaxy1_y = galaxy1_location
        galaxy2_x, galaxy2_y = galaxy2_location
        distance = abs(galaxy1_x - galaxy2_x) + abs(galaxy1_y - galaxy2_y)
        return distance

    def expand(self):
        self.expand_cols()
        self.expand_rows()

    def expand_rows(self):
        rows_to_expand = []
        for i in range(len(self.image)):
            row = self.image[i]
            if self.can_expand(row):
                rows_to_expand.append(i)

        for row_index in reversed(rows_to_expand):
            self.expand_row(row_index)

    def expand_row(self, row_index):
        row = self.image[row_index]
        self.image.insert(row_index, row)

    def expand_cols(self):
        cols_to_expand = []
        for i in range(len(self.image[0])):
            col = self.extract_col(self.image, i)
            if self.can_expand(col):
                cols_to_expand.append(i)

        for col_index in reversed(cols_to_expand):
            self.expand_col(col_index)

    def expand_col(self, col_index):
        for row in self.image:
            row.insert(col_index, '.')

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


def part1(input='day11/input'):
    image = load(input)
    cosmic_image = CosmicImage(image)
    cosmic_image.expand()
    cosmic_image.tag()
    cosmic_image.calc_permutations()
    return cosmic_image.calc_sum_distances()


def print_array(loop):
    print('')
    for row in loop:
        for i in row:
            print(i, end='')
        print('')


if __name__ == '__main__':
    print(part1())
