
cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def idValue(line):
    valid = True

    line = line.strip()
    id, sets = line.split(':')
    s, id = id.split(' ')
    id = int(id)

    sets = sets.split(';')

    for s in sets:
        s = s.split(',')
        for pick in s:
            pick = pick.strip()
            qty, color = pick.split(' ')
            qty = int(qty)
            color = color.strip()
            if cubes[color] < qty:
                valid = False

    return id if valid else 0


sumPossible = 0

inputFile = open('input', 'r')

for line in inputFile:
    sumPossible += idValue(line)

print(sumPossible)
