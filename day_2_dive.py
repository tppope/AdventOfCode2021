def getSimplePosition(inputDirectory):
    depth = 0
    horizontalPos = 0
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            command = line.split()[0]
            length = int(line.split()[1])
            if command == "forward":
                horizontalPos += length
            elif command == "down":
                depth += length
            elif command == "up":
                depth -= length
            line = file.readline()
    return depth * horizontalPos


def getHarderPosition(inputDirectory):
    depth = 0
    horizontalPos = 0
    aim = 0
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            command = line.split()[0]
            length = int(line.split()[1])
            if command == "forward":
                horizontalPos += length
                depth += aim*length
            elif command == "down":
                aim += length
            elif command == "up":
                aim -= length
            line = file.readline()
    return depth * horizontalPos


def getAnswerPart1(inputDirectory):
    return getSimplePosition(inputDirectory)


def getAnswerPart2(inputDirectory):
    return getHarderPosition(inputDirectory)
