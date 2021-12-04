def getFinalBoardScore(inputDirectory):
    drawNumbers = getDrawNumbers(inputDirectory)
    boards = getBoards(inputDirectory)
    for number in drawNumbers:
        boardsToDelete = []
        for key in boards:
            for row in boards[key]:
                if int(number) in row:
                    row[int(number)] = True
            if checkWinningBoard(boards[key]):
                if len(boards) == 1:
                    return getBoardScore(boards.popitem()[1], int(number))
                boardsToDelete.append(key)
        for toDelete in boardsToDelete:
            boards.pop(toDelete)

    return 0


def checkWinningBoard(board):
    columnTruth = [True] * len(board[0])
    for row in board:
        rowIsTrue = True
        columnIndex = 0
        for key in row:
            if not row[key]:
                rowIsTrue = False
                columnTruth[columnIndex] = False
            columnIndex += 1
        if rowIsTrue:
            return True
    for truth in columnTruth:
        if truth:
            return True
    return False


def getBoardScore(board, number):
    unmarkedSum = 0
    for row in board:
        for key in row:
            if not row[key]:
                unmarkedSum += key
    return number * unmarkedSum


def getBoards(inputDirectory):
    boards = dict()
    board = []
    boardIndex = 0
    with open(inputDirectory) as file:
        file.readline()
        line = file.readline()
        while line:
            if line == "\n":
                boards[boardIndex] = board
                boardIndex += 1
                board = []
                line = file.readline()
            else:
                boardRow = dict()
                row = line.split()
                for element in row:
                    boardRow[int(element)] = False
                board.append(boardRow)
                line = file.readline()
        boards[boardIndex] = board
        del boards[0]
        return boards


def getDrawNumbers(inputDirectory):
    with open(inputDirectory) as file:
        line = file.readline()
    drawNumbers = line.split(",")
    drawNumbers[-1] = drawNumbers[-1][:-1]
    return drawNumbers


def getAnswer(inputDirectory):
    return getFinalBoardScore(inputDirectory)
