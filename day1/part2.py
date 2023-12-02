import re
inputFile = open('input', 'r')


def startWordDigit(line, word, digit):
    if line.startswith(word):
        line = line.replace(word[0], digit, 1)
    return line


def getCalibrationValue(line):
    line = line.strip()

    convertedLine = ''

    while line != '':
        line = startWordDigit(line, 'one', '1')
        line = startWordDigit(line, 'two', '2')
        line = startWordDigit(line, 'three', '3')
        line = startWordDigit(line, 'four', '4')
        line = startWordDigit(line, 'five', '5')
        line = startWordDigit(line, 'six', '6')
        line = startWordDigit(line, 'seven', '7')
        line = startWordDigit(line, 'eight', '8')
        line = startWordDigit(line, 'nine', '9')
        convertedLine += line[0]
        line = line[1:]

    digits = re.sub('[^1-9]', '', convertedLine)
    firstD = digits[0]
    lastD = digits[-1]
    return int(str(firstD) + str(lastD))


sumCalibration = 0

for line in inputFile.readlines():
    sumCalibration += getCalibrationValue(line)

print(sumCalibration)
