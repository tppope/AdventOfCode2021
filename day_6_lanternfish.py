def lanternfishCount(inputDirectory):
    lanternFishes = getLanternfishes(inputDirectory)
    for day in range(80):
        for j in range(len(lanternFishes)):
            if lanternFishes[j] == 0:
                lanternFishes[j] = 6
                lanternFishes.append(8)
            else:
                lanternFishes[j] -= 1

    return len(lanternFishes)


def newLanternfishCount(inputDirectory):
    lanternFishes = getLanternfishes(inputDirectory)
    timerCounter = getTimerCounter(lanternFishes)
    for day in range(256):
        updateTimerCounter(timerCounter)
    return sum(timerCounter)


def updateTimerCounter(timerCounter):
    sixTimerCount = timerCounter[0]
    eightTimerCount = timerCounter[8]
    for i in range(-1, len(timerCounter) - 2):
        timerCounter[i] = timerCounter[i + 1]
    timerCounter[7] = eightTimerCount
    timerCounter[6] += sixTimerCount


def getTimerCounter(lanternFishes):
    timerCounter = [0] * 9
    for lanternfish in lanternFishes:
        timerCounter[lanternfish] += 1
    return timerCounter


def getLanternfishes(inputDirectory):
    with open(inputDirectory) as file:
        line = file.read()
    lanternFishes = list(map(int, line.split(',')))
    return lanternFishes


def getAnswerPart1(inputDirectory):
    return lanternfishCount(inputDirectory)


def getAnswerPart2(inputDirectory):
    return newLanternfishCount(inputDirectory)
