import re
inputFile = open('input', 'r')

sumCalibration = 0

for line in inputFile:
    digits = re.sub('\\D', '', line)
    firstD = digits[0]
    lastD = digits[-1]
    calibrationValue = firstD + lastD
    sumCalibration += int(calibrationValue)

print(sumCalibration)
