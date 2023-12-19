import subprocess
import copy
import time


def drawbeam(contraption, beams):
    alive_locations = [beam.location for beam in beams if beam.is_alive]
    _map = copy.deepcopy(contraption.map)

    for col, row in alive_locations:
        _map[row][col] = '@'

    print_array(_map)
    time.sleep(0.1)


def print_array(array):

    subprocess.call("clear")
    for line in array:
        print(''.join(line))
