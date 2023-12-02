def powerValue(line):

    line = line.strip()
    id, sets = line.split(':')
    s, id = id.split(' ')
    id = int(id)

    sets = sets.split(';')

    cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for s in sets:
        s = s.split(',')
        for pick in s:
            pick = pick.strip()
            qty, color = pick.split(' ')
            qty = int(qty)
            color = color.strip()
            if cubes[color] < qty:
                cubes[color] = qty

    return cubes['red']*cubes['green']*cubes['blue']


sumPossible = 0

inputFile = open('input', 'r')

for line in inputFile:
    sumPossible += powerValue(line)

print(sumPossible)
