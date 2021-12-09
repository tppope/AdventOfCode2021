def getRiskLevelSum(inputDirectory):
    riskLevelSum = 0
    heatmap = getHeatmap(inputDirectory)
    maxRows = len(heatmap)
    maxColumns = len(heatmap[0])
    for row in range(maxRows):
        for column in range(maxColumns):
            lowPoint = heatmap[row][column]
            if checkLowPoint(lowPoint, heatmap, row, column, maxRows - 1, maxColumns - 1):
                riskLevelSum += lowPoint + 1
    return riskLevelSum


def checkLowPoint(lowPoint, heatmap, row, column, maxRows, maxColumns):
    if row == 0:
        if column == 0:
            return checkLeftTopCorner(lowPoint, heatmap, row, column)
        if column == maxColumns:
            return checkRightTopCorner(lowPoint, heatmap, row, column)
        return lowPoint < heatmap[row][column + 1] and checkRightTopCorner(lowPoint, heatmap, row, column)
    if row == maxRows:
        if column == 0:
            return checkLeftBottomCorner(lowPoint, heatmap, row, column)
        if column == maxColumns:
            return checkRightBottomCorner(lowPoint, heatmap, row, column)
        return lowPoint < heatmap[row][column + 1] and checkRightBottomCorner(lowPoint, heatmap, row, column)
    if column == 0:
        return lowPoint < heatmap[row - 1][column] and checkLeftTopCorner(lowPoint, heatmap, row, column)
    if column == maxColumns:
        return lowPoint < heatmap[row - 1][column] and checkRightTopCorner(lowPoint, heatmap, row, column)
    return checkLeftTopCorner(lowPoint, heatmap, row, column) and checkRightBottomCorner(lowPoint, heatmap, row, column)


def checkLeftTopCorner(lowPoint, heatmap, row, column):
    return lowPoint < heatmap[row + 1][column] and lowPoint < heatmap[row][column + 1]


def checkRightTopCorner(lowPoint, heatmap, row, column):
    return lowPoint < heatmap[row + 1][column] and lowPoint < heatmap[row][column - 1]


def checkLeftBottomCorner(lowPoint, heatmap, row, column):
    return lowPoint < heatmap[row - 1][column] and lowPoint < heatmap[row][column + 1]


def checkRightBottomCorner(lowPoint, heatmap, row, column):
    return lowPoint < heatmap[row - 1][column] and lowPoint < heatmap[row][column - 1]


def getHeatmap(inputDirectory):
    heatmap = []
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            heatmap.append(list(map(int, list(line.strip()))))
            line = file.readline()
    return heatmap


def getThreeLargestBasineMultiply(inputDirectory):
    threeLargestBasine = [0] * 3
    heatmap = getHeatmap(inputDirectory)
    maxRows = len(heatmap)
    maxColumns = len(heatmap[0])
    for row in range(maxRows):
        for column in range(maxColumns):
            lowPoint = heatmap[row][column]
            if checkLowPoint(lowPoint, heatmap, row, column, maxRows - 1, maxColumns - 1):
                alreadyAttended = []
                basine = recurBasine(lowPoint, heatmap, row, column, maxRows, maxColumns, alreadyAttended)
                checkThreeLargestBasine(threeLargestBasine, basine)
    return makeThreeLargestBasineMultiply(threeLargestBasine)


def recurBasine(lowPoint, heatmap, row, column, maxRows, maxColumns, alreadyAttended):
    alreadyAttended.append([row, column])
    count = 1
    if lowPoint == 9:
        return 0
    if row + 1 < maxRows and [row + 1, column] not in alreadyAttended:
        count += recurBasine(heatmap[row + 1][column], heatmap, row + 1, column, maxRows, maxColumns, alreadyAttended)
    if row - 1 >= 0 and [row - 1, column] not in alreadyAttended:
        count += recurBasine(heatmap[row - 1][column], heatmap, row - 1, column, maxRows, maxColumns, alreadyAttended)
    if column + 1 < maxColumns and [row, column + 1] not in alreadyAttended:
        count += recurBasine(heatmap[row][column + 1], heatmap, row, column + 1, maxRows, maxColumns, alreadyAttended)
    if column - 1 >= 0 and [row, column - 1] not in alreadyAttended:
        count += recurBasine(heatmap[row][column - 1], heatmap, row, column - 1, maxRows, maxColumns, alreadyAttended)
    return count


def makeThreeLargestBasineMultiply(threeLargestBasine):
    threeLargestBasineMultiply = 1
    for basine in threeLargestBasine:
        threeLargestBasineMultiply *= basine
    return threeLargestBasineMultiply


def checkThreeLargestBasine(threeLargestBasine, basine):
    if min(threeLargestBasine) < basine:
        threeLargestBasine[threeLargestBasine.index(min(threeLargestBasine))] = basine


def getAnswerPart1(inputDirectory):
    return getRiskLevelSum(inputDirectory)


def getAnswerPart2(inputDirectory):
    return getThreeLargestBasineMultiply(inputDirectory)
