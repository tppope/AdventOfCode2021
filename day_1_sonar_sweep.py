def higherMeasurementsCount(inputDirectory):
    measurementsCount = 0
    with open(inputDirectory) as file:
        line = file.readline()
        measurement = int(line)
        while True:
            line = file.readline()
            if line == "":
                break
            if int(line) > measurement:
                measurementsCount += 1
            measurement = int(line)
    return measurementsCount


def higherSumMeasurementsCount(inputDirectory):
    measurementsCount = 0
    measurements = getMeasurementsArray(inputDirectory)
    for index in range(len(measurements)):
        if index > 2:
            threeSumA = measurements[index - 1] + measurements[index - 2] + measurements[index - 3]
            threeSumB = measurements[index] + measurements[index - 1] + measurements[index - 2]
            if threeSumB > threeSumA:
                measurementsCount += 1

    return measurementsCount


def getMeasurementsArray(inputDirectory):
    measurements = []
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            measurements.append(int(line))
            line = file.readline()
    return measurements


def getAnswerPart1(inputDirectory):
    return higherMeasurementsCount(inputDirectory)


def getAnswerPart2(inputDirectory):
    return higherSumMeasurementsCount(inputDirectory)
