from enum import Enum

from typing import Tuple, List, Optional

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Elements(Enum):
    EMPTY_SPACE = '.'
    MIRROR_SLASH = '/'
    MIRROR_BACKSLASH = '\\'
    SPLITTER_VERTICAL = '|'
    SPLITTER_HORIZONTAL = '-'


class Contraption():
    def __init__(self, map: List[List[str]]) -> None:
        self.map = Contraption.parse_map(map)
        self.width = len(map[0])
        self.height = len(map)
        self.splits = set()
        self.bounces = set()

    def is_inside(self, x_y: Tuple[int, int]) -> bool:
        if x_y is None:
            return False
        x, y = x_y
        return x in range(self.width) and y in range(self.height)

    def get_element(self, x_y: Tuple[int, int]) -> Elements:
        if self.is_inside(x_y):
            col, row = x_y
            return Elements(self.map[row][col])

    def has_element_split(self, location):
        return location in self.splits

    def set_element_split(self, location):
        self.splits.add(location)

    def has_bounced_directional(self, location, direction) -> bool:
        return (location, direction) in self.bounces

    def set_bounced_directional(self, location, direction) -> bool:
        self.bounces.add((location, direction))

    @staticmethod
    def parse_map(map) -> List[List[str]]:
        return [list(line) for line in map]


class Beam():

    def __init__(self, contraption: Contraption,
                 start_x: int, start_y: int,
                 direction: Tuple[int, int]) -> None:
        self.x = start_x
        self.y = start_y
        self.direction = direction
        self.contraption = contraption
        self.is_alive = True
        self.breadcrumbs = set()

    @property
    def location(self) -> Optional[Tuple[int, int]]:
        if self.contraption.is_inside((self.x, self.y)):
            return (self.x, self.y)

    @property
    def element(self) -> Optional[Elements]:
        return self.contraption.get_element(self.location)

    @staticmethod
    def bounce(element: Elements, direction: Tuple[int, int]) -> Elements:
        if element == Elements.MIRROR_SLASH:
            if direction == UP:
                return RIGHT
            if direction == DOWN:
                return LEFT
            if direction == LEFT:
                return DOWN
            if direction == RIGHT:
                return UP
        elif element == Elements.MIRROR_BACKSLASH:
            if direction == UP:
                return LEFT
            if direction == DOWN:
                return RIGHT
            if direction == LEFT:
                return UP
            if direction == RIGHT:
                return DOWN

    def step(self) -> Optional[List['Beam']]:

        dir = self.direction

        dx, dy = self.direction

        self.x += dx
        self.y += dy

        location = self.location
        if location is None:
            self.is_alive = False
        else:
            self.breadcrumbs.add(location)

        element = self.element

        if element == Elements.SPLITTER_VERTICAL and (self.direction == LEFT or self.direction == RIGHT):
            if not self.contraption.has_element_split(self.location):
                self.contraption.set_element_split(self.location)
                beam_up = Beam(self.contraption, self.x, self.y, UP)
                beam_down = Beam(self.contraption, self.x, self.y, DOWN)
                self.is_alive = False
                return [beam_up, beam_down]
        elif element == Elements.SPLITTER_HORIZONTAL and (self.direction == UP or self.direction == DOWN):
            if not self.contraption.has_element_split(self.location):
                self.contraption.set_element_split(self.location)
                beam_left = Beam(self.contraption, self.x, self.y, LEFT)
                beam_right = Beam(self.contraption, self.x, self.y, RIGHT)
                self.is_alive = False
                return [beam_left, beam_right]
        elif element == Elements.MIRROR_SLASH or element == Elements.MIRROR_BACKSLASH:
            if not self.contraption.has_bounced_directional(self.location, dir):
                self.contraption.set_bounced_directional(self.location, dir)
                self.direction = Beam.bounce(element, self.direction)
            else:
                self.is_alive = False


def part1(input='day16/input.txt'):
    _map = []
    with open(input, 'r') as file:
        _map = [line.strip() for line in file.readlines()]

    contraption = Contraption(_map)

    beams = [Beam(contraption, -1, 0, RIGHT)]

    while True:
        new_beams = []
        for beam in beams:
            if beam.is_alive:
                result = beam.step()
                if result:
                    new_beams.extend(result)

        beams.extend(new_beams)

        if all(not beam.is_alive for beam in beams):
            break

    merged_breadcrumbs = set()
    for beam in beams:
        merged_breadcrumbs.update(beam.breadcrumbs)

    print(f"beam count: {len(beams)}")

    return len(merged_breadcrumbs)


def part2():
    pass


if __name__ == '__main__':
    print(part1())
    print(part2())
