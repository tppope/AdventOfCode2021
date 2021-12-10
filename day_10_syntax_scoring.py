def getTotalSyntaxErrorScore(inputDirectory):
    chunksPair = {"(": ")", "{": "}", "[": "]", "<": ">"}
    chunksErrorScore = {")": 3, "}": 1197, "]": 57, ">": 25137}
    totalSyntaxErrorScore = 0
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            openChunks = []
            for character in list(line.strip()):
                if character in chunksPair.keys():
                    openChunks.append(character)
                elif character != chunksPair[openChunks.pop()]:
                    totalSyntaxErrorScore += chunksErrorScore[character]
                    break
            line = file.readline()
    return totalSyntaxErrorScore


def getMiddleScore(inputDirectory):
    chunksPair = {"(": ")", "{": "}", "[": "]", "<": ">"}
    totalMiddleScores = []
    with open(inputDirectory) as file:
        line = file.readline()
        while line:
            openChunks = []
            incompleteLine = True
            for character in list(line.strip()):
                if character in chunksPair.keys():
                    openChunks.append(character)
                elif character != chunksPair[openChunks.pop()]:
                    incompleteLine = False
                    break
            if incompleteLine:
                totalMiddleScores.append(getScore(openChunks))
            line = file.readline()
    totalMiddleScores.sort()
    return totalMiddleScores[int(len(totalMiddleScores) / 2)]


def getScore(openChunks):
    chunksMiddleScore = {"(": 1, "[": 2, "{": 3, "<": 4}
    score = 0
    while openChunks:
        score *= 5
        score += chunksMiddleScore[openChunks.pop()]
    return score


def getAnswerPart1(inputDirectory):
    return getTotalSyntaxErrorScore(inputDirectory)


def getAnswerPart2(inputDirectory):
    return getMiddleScore(inputDirectory)
