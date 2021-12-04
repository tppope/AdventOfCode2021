def getPowerConsumption(inputDirectory):
    zeroCount = []
    oneCount = []
    with open(inputDirectory) as file:
        line = file.readline()
        zeroCount = [0] * (len(line) - 1)
        oneCount = [0] * (len(line) - 1)
        while line:
            for i in range(len(line) - 1):
                if int(line[i]):
                    oneCount[i] += 1
                else:
                    zeroCount[i] += 1
            line = file.readline()
    return calculatePowerConsumption(zeroCount, oneCount)


def calculatePowerConsumption(zeroCount, oneCount):
    gammaRate = ""
    epsilonRate = ""
    for i in range(len(zeroCount)):
        if zeroCount[i] > oneCount[i]:
            gammaRate += "0"
            epsilonRate += "1"
        elif zeroCount[i] < oneCount[i]:
            gammaRate += "1"
            epsilonRate += "0"
    return int(gammaRate, 2) * int(epsilonRate, 2)


def reduceBinDescArray(binDescArray, position, bit):
    newBinDescArray = []
    for element in binDescArray:
        if int(element[position]) == bit:
            newBinDescArray.append(element)
    return newBinDescArray


def getCommonBit(binDescArray, position, wantMostCommon):
    oneCount = 0
    zeroCount = 0
    for element in binDescArray:
        if int(element[position]):
            oneCount += 1
        else:
            zeroCount += 1
    if wantMostCommon:
        return getMostCommonBit(oneCount, zeroCount)
    else:
        return getLeastCommonBit(oneCount, zeroCount)


def getMostCommonBit(oneCount, zeroCount):
    if oneCount >= zeroCount:
        return 1
    else:
        return 0


def getLeastCommonBit(oneCount, zeroCount):
    if oneCount >= zeroCount:
        return 0
    else:
        return 1


def getOxygenGeneratorRating(binDescArray):
    position = 0
    while len(binDescArray) > 1:
        binDescArray = reduceBinDescArray(binDescArray, position, getCommonBit(binDescArray, position, True))
        position += 1
    return int(binDescArray[0], 2)


def getCO2ScrubberRating(binDescArray):
    position = 0
    while len(binDescArray) > 1:
        binDescArray = reduceBinDescArray(binDescArray, position, getCommonBit(binDescArray, position, False))
        position += 1
    return int(binDescArray[0], 2)


def getLifeSupportRating(inputDirectory):
    binDescArray = getBinDescArray(inputDirectory)
    oxygenGeneratorRating = getOxygenGeneratorRating(binDescArray)
    co2ScrubberRating = getCO2ScrubberRating(binDescArray)
    return oxygenGeneratorRating * co2ScrubberRating


def getBinDescArray(inputDirectory):
    binDescArray = []
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            binDescArray.append(line[:-1])
            line = file.readline()
    return binDescArray


def getAnswerPart1(inputDirectory):
    return getPowerConsumption(inputDirectory)


def getAnswerPart2(inputDirectory):
    return getLifeSupportRating(inputDirectory)
