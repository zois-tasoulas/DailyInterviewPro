def findWord(matrix, word):
    numberOfColumns = len(matrix[0])
    numberOfRows = len(matrix)
    wordLength = len(word)
    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            if matrix[i][j] == word[0]:
                if i < numberOfRows - wordLength + 1:
                    if checkWordVertically(matrix, i, j, word):
                        return True
                if j < numberOfColumns - wordLength + 1:
                    if checkWordHorizontally(matrix, i, j, word):
                        return True
    return False

def checkWordVertically(matrix, row, column, word):
    for letter in word:
        if letter != matrix[row][column]:
            return False
        row += 1
    return True

def checkWordHorizontally(matrix, row, column, word):
    for letter in word:
        if letter != matrix[row][column]:
            return False
        column += 1
    return True

if __name__ == '__main__':
    matrix = [['A', 'C', 'A', 'T', 'M'],
              ['Q', 'A', 'Q', 'P', 'I'],
              ['W', 'R', 'O', 'N', 'L'],
              ['A', 'N', 'I', 'S', 'K'],
              ['F', 'T', 'A', 'C', 'L'],
              ['V', 'K', 'R', 'U', 'N']]
    word = "RUN"
    print(findWord(matrix, word))
    word = "RAT"
    print(findWord(matrix, word))
