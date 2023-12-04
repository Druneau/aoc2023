from itertools import groupby
from operator import itemgetter


def IdxDigits(line):
    digitIndices = [pos for pos, char in enumerate(line) if char.isdigit()]

    # group masked digit indices into actual part numbers (consecutive digits as lists)
    groups = []
    for k, g in groupby(enumerate(digitIndices), lambda i_x: i_x[0] - i_x[1]):
        groups.append(list(map(itemgetter(1), g)))
    return groups


def IdxStar(line):
    starIndices = [pos for pos, char in enumerate(line) if char == '*']
    return starIndices


def getGearNumber(line, digits):
    n = ''
    for i in digits:
        n += line[i]
    return int(n)


def validGearPart(line, sB, sC, sA, lineNumber):

    digits = IdxDigits(line)

    # build a list of parts that touch a gear (star) while keeping reference
    # to which exact gear (line number and index)
    parts = []
    for g in sB:
        for d in digits:
            if any(x in [g-1, g, g+1] for x in d):
                parts.append(
                    (str(g) + '-' + str(lineNumber-1), (getGearNumber(line, d), lineNumber)))
    for g in sC:
        for d in digits:
            if any(x in [g-1, g, g+1] for x in d):
                parts.append((str(g) + '-' + str(lineNumber),
                             (getGearNumber(line, d), lineNumber)))
    for g in sA:
        for d in digits:
            if any(x in [g-1, g, g+1] for x in d):
                parts.append(
                    (str(g) + '-' + str(lineNumber+1), (getGearNumber(line, d), lineNumber)))

    return parts


starsDict = {}
sumGearRatios = 0
lineNumber = 0

with open('day3/input', 'r') as file:
    lineBefore = ''
    lineCurrent = ''

    for line in file:
        line = line.strip()

        if lineCurrent != '':

            # Get Merged 'contact' indices where special characters can touch, current line and previous line?
            starBefore = IdxStar(lineBefore)
            starCurrent = IdxStar(lineCurrent)
            starAfter = IdxStar(line)

            parts = validGearPart(lineCurrent,
                                  starBefore, starCurrent, starAfter, lineNumber)

            for g, n in parts:
                if g in starsDict:
                    starsDict[g].append(n)
                else:
                    starsDict[g] = [n]

        lineNumber += 1
        lineBefore = lineCurrent
        lineCurrent = line

    # for last line
    # Get Merged 'contact' indices where special characters can touch, current line and previous line?
    starBefore = IdxStar(lineBefore)
    starCurrent = IdxStar(lineCurrent)
    starAfter = IdxStar(line)

    parts = validGearPart(lineCurrent,
                          starBefore, starCurrent, starAfter, lineNumber)

    for g, n in parts:
        if g in starsDict:
            starsDict[g].append(n)
        else:
            starsDict[g] = n

    for key, val in starsDict.items():
        if len(val) == 2:
            sumGearRatios += val[0][0]*val[1][0]

print(sumGearRatios)
