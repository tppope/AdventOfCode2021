def getPointsCountWithTwoAndMoreOverlaps(inputDirectory):
    passedPoints = []
    twoTimesInPassedPoints = []
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            line = line.replace(" ", "")
            fromPoint = line.split("->")[0]
            toPoint = line.split("->")[1]
            getPassedPoints(fromPoint, toPoint, passedPoints, twoTimesInPassedPoints)
            line = file.readline()
    return len(twoTimesInPassedPoints)


def getPassedPoints(fromPoint, toPoint, passedPoints, twoTimesInPassedPoints):
    if int(fromPoint.split(",")[0]) == int(toPoint.split(",")[0]):
        if int(fromPoint.split(",")[1]) < int(toPoint.split(",")[1]):
            for i in range(int(fromPoint.split(",")[1]), int(toPoint.split(",")[1]) + 1):
                insertToPassedPoints(int(fromPoint.split(",")[0]), i, passedPoints, twoTimesInPassedPoints)
        else:
            for i in range(int(fromPoint.split(",")[1]), int(toPoint.split(",")[1]) - 1, -1):
                insertToPassedPoints(int(fromPoint.split(",")[0]), i, passedPoints,
                                     twoTimesInPassedPoints)
    elif int(fromPoint.split(",")[1]) == int(toPoint.split(",")[1]):
        if int(fromPoint.split(",")[0]) < int(toPoint.split(",")[0]):
            for i in range(int(fromPoint.split(",")[0]), int(toPoint.split(",")[0]) + 1):
                insertToPassedPoints(i, int(fromPoint.split(",")[1]), passedPoints,
                                     twoTimesInPassedPoints)
        else:
            for i in range(int(fromPoint.split(",")[0]), int(toPoint.split(",")[0]) - 1, -1):
                insertToPassedPoints(i, int(fromPoint.split(",")[1]), passedPoints,
                                     twoTimesInPassedPoints)
    else:
        rangeBetween = abs(int(fromPoint.split(",")[0]) - int(toPoint.split(",")[0]))
        for i in range(rangeBetween + 1):
            if int(fromPoint.split(",")[0]) < int(toPoint.split(",")[0]):
                if int(fromPoint.split(",")[1]) < int(toPoint.split(",")[1]):
                    insertToPassedPoints(int(fromPoint.split(",")[0]) + i, int(fromPoint.split(",")[1]) + i,
                                         passedPoints, twoTimesInPassedPoints)
                else:
                    insertToPassedPoints(int(fromPoint.split(",")[0]) + i, int(fromPoint.split(",")[1]) - i,
                                         passedPoints, twoTimesInPassedPoints)
            else:
                if int(fromPoint.split(",")[1]) < int(toPoint.split(",")[1]):
                    insertToPassedPoints(int(fromPoint.split(",")[0]) - i, int(fromPoint.split(",")[1]) + i,
                                         passedPoints, twoTimesInPassedPoints)
                else:
                    insertToPassedPoints(int(fromPoint.split(",")[0]) - i, int(fromPoint.split(",")[1]) - i,
                                         passedPoints, twoTimesInPassedPoints)


def insertToPassedPoints(x, y, passedPoints, twoTimesInPassedPoints):
    if (str(x) + "," + str(y)) not in passedPoints:
        passedPoints.append((str(x) + "," + str(y)))
    else:
        if (str(x) + "," + str(y)) not in twoTimesInPassedPoints:
            twoTimesInPassedPoints.append((str(x) + "," + str(y)))


def getAnswerPart1(inputDirectory):
    return getPointsCountWithTwoAndMoreOverlaps(inputDirectory)
