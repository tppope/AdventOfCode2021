def getCrabsMustSpendFuel(inputDirectory):
    positions = getPositions(inputDirectory)
    maxPos = max(positions)
    minFuel = 0
    for i in range(maxPos + 1):
        fuelSum = 0
        for j in range(len(positions)):
            fuelSum += getBurnFuel(abs(positions[j] - i))
        if i == 0:
            minFuel = fuelSum
        else:
            if minFuel > fuelSum:
                minFuel = fuelSum
    return minFuel


def getBurnFuel(steps):
    burnFuel = 0
    for i in range(steps + 1):
        burnFuel += i
    return burnFuel


def getPositions(inputDirectory):
    with open(inputDirectory) as file:
        line = file.read()
    positions = list(map(int, line.split(',')))
    return positions


def getAnswer(inputDirectory):
    return getCrabsMustSpendFuel(inputDirectory)
