def getEasyDigitsCount(inputDirectory):
    easyDigitsCount = 0
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            for digit in line.split("|")[1].split(" "):
                if 1 < len(digit.strip()) < 5 or len(digit.strip()) == 7:
                    easyDigitsCount += 1
            line = file.readline()
    return easyDigitsCount


def getOutputValuesSum(inputDirectory):
    outputValuesSum = 0
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            dictionary = getDictionary(line.split("|")[0])
            outputValuesSum += getOutputValue(line.split("|")[1].strip(), dictionary)
            line = file.readline()
    return outputValuesSum


def getOutputValue(outputPart, dictionary):
    number = ""
    for digit in outputPart.split(" "):
        number += translateDigitToNumber(dictionary, digit.strip())
    return int(number)


def translateDigitToNumber(dictionary, digit):
    for translation in dictionary:
        if len(digit) == len(dictionary[translation]) and digitsDifference(digit, dictionary[translation]) == "":
            return translation


def getDictionary(deductivePart):
    dictionary = dict()
    dictionary["1"] = getNumberOne(deductivePart)
    dictionary["7"] = getNumberSeven(deductivePart)
    dictionary["4"] = getNumberFour(deductivePart)
    dictionary["8"] = getNumberEight(deductivePart)
    dictionary["0"] = getNumberZero(deductivePart, digitsDifference(dictionary["1"], dictionary["4"]))
    dictionary["9"] = getNumberNine(deductivePart, dictionary["4"])
    dictionary["6"] = getNumberSix(deductivePart, dictionary["9"], dictionary["0"])
    dictionary["5"] = getNumberFive(deductivePart, digitsDifference(
        digitsDifference(dictionary["9"], dictionary["8"]), dictionary["6"]))
    dictionary["2"] = getNumberTwo(deductivePart, dictionary["9"])
    dictionary["3"] = getNumberThree(deductivePart, dictionary["5"], dictionary["2"])
    return dictionary


def digitsDifference(firstDigit, secondDigit):
    for c in firstDigit:
        secondDigit = secondDigit.replace(c, "")
    return secondDigit


def getNumberFive(deductivePart, difference):
    for digit in deductivePart.split(" "):
        if len(digit) == 5 and (0 not in [c in digit for c in difference]):
            return digit


def getNumberThree(deductivePart, numberFive, numberTwo):
    for digit in deductivePart.split(" "):
        if len(digit) == 5 and digit != numberFive and digit != numberTwo:
            return digit


def getNumberTwo(deductivePart, numberNine):
    for digit in deductivePart.split(" "):
        if len(digit) == 5 and len(digitsDifference(digit, numberNine)) == 2:
            return digit


def getNumberSix(deductivePart, numberNine, numberZero):
    for digit in deductivePart.split(" "):
        if len(digit) == 6 and digit != numberNine and digit != numberZero:
            return digit


def getNumberNine(deductivePart, numberFour):
    for digit in deductivePart.split(" "):
        if len(digit) == 6 and (0 not in [c in digit for c in numberFour]):
            return digit


def getNumberZero(deductivePart, difference):
    for digit in deductivePart.split(" "):
        if len(digit) == 6 and (0 in [c in digit for c in difference]):
            return digit


def getNumberOne(deductivePart):
    for digit in deductivePart.split(" "):
        if len(digit) == 2:
            return digit


def getNumberSeven(deductivePart):
    for digit in deductivePart.split(" "):
        if len(digit) == 3:
            return digit


def getNumberFour(deductivePart):
    for digit in deductivePart.split(" "):
        if len(digit) == 4:
            return digit


def getNumberEight(deductivePart):
    for digit in deductivePart.split(" "):
        if len(digit) == 7:
            return digit


def getAnswerPart1(inputDirectory):
    return getEasyDigitsCount(inputDirectory)


def getAnswerPart2(inputDirectory):
    return getOutputValuesSum(inputDirectory)
