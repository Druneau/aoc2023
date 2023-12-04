from itertools import groupby
from operator import itemgetter


def IdxDigits(line):
    digitIndices = [pos for pos, char in enumerate(line) if char.isdigit()]

    # group masked digit indices into actual part numbers (consecutive digits as lists)
    groups = []
    for k, g in groupby(enumerate(digitIndices), lambda i_x: i_x[0] - i_x[1]):
        groups.append(list(map(itemgetter(1), g)))
    return groups


def IdxContact(line):
    specialIndices = [pos for pos, char in enumerate(
        line) if not (char == '.' or char.isdigit())]
    specialAdjacent = []
    for i in specialIndices:
        specialAdjacent.extend([i-1, i, i+1])
    specialAdjacent = [max(min(x, 139), 0) for x in specialAdjacent]
    specialAdjacent = list(set(specialAdjacent))
    specialAdjacent.sort()
    return specialAdjacent


def validParts(line, digits, contact):

    # Match contact indices to digits
    parts = []
    if contact is None:
        return parts
    for part in digits:
        for d in part:
            if d in contact:
                parts.append(part)
    uniqueParts = [list(x) for x in set(tuple(x) for x in parts)]

    # Convert digit indices to part numbers
    parts = []
    for p in uniqueParts:
        n = ''
        for i in p:
            n += line[i]
        parts.append(int(n))

    return parts


sumPartNumbers = 0

with open('day3/input', 'r') as file:
    lineBefore = ''
    lineCurrent = ''

    for line in file:
        line = line.strip()

        if lineCurrent != '':
            # Get list of location of digits
            digitLocations = IdxDigits(lineCurrent)

            # Get Merged 'contact' indices where special characters can touch, current line and previous line?
            symBefore = IdxContact(lineBefore)
            symCurrent = IdxContact(lineCurrent)
            symAfter = IdxContact(line)

            symMerged = list(set(symBefore+symCurrent+symAfter))
            symMerged.sort()

            parts = validParts(lineCurrent,
                               digitLocations, symMerged)

            sumPartNumbers += sum(parts)

        lineBefore = lineCurrent
        lineCurrent = line

    # for last line
    # Get list of location of digits
    digitLocations = IdxDigits(lineCurrent)

    # Get Merged 'contact' indices where special characters can touch, current line and previous line?
    symBefore = IdxContact(lineBefore)
    symCurrent = IdxContact(lineCurrent)
    symMerged = list(set(symBefore+symCurrent+symAfter))
    symMerged.sort()

    parts = validParts(lineCurrent,
                       digitLocations, symMerged)

    sumPartNumbers += sum(parts)


print(sumPartNumbers)
