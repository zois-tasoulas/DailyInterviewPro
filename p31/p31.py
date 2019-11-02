class Solution:
    def printSpiralTraversal(self, matrix):
        numOfRows = len(matrix)
        numOfColumns = len(matrix[0])
        if numOfColumns > 1:
            direction = 0
        else:
            direction = 1
        rowIndex = 0
        columnIndex = 0
        rightBorder = numOfColumns - 1
        bottomBorder = numOfRows - 1
        leftBorder = 0
        topBorder = 1
        print(matrix[rowIndex][columnIndex], end='')
        for _ in range(numOfRows * numOfColumns - 1):
            print(", ", end='')
            if direction == 0:        #Print element to the right
                print(matrix[rowIndex][columnIndex + 1], end='')
                if columnIndex + 1 == rightBorder:
                    rightBorder = columnIndex
                    direction = 1
                columnIndex += 1
            elif direction == 1:      #Print element on the bottom
                print(matrix[rowIndex + 1][columnIndex], end='')
                if rowIndex + 1 == bottomBorder:
                    bottomBorder = rowIndex
                    direction = 2
                rowIndex += 1
            elif direction == 2:      #Print element to the left
                print(matrix[rowIndex][columnIndex - 1], end='')
                if columnIndex - 1 == leftBorder:
                    leftBorder = columnIndex
                    direction = 3
                columnIndex -= 1
            else:                     #Print element on the top
                print(matrix[rowIndex - 1][columnIndex], end='')
                if rowIndex - 1 == topBorder:
                    topBorder = rowIndex
                    direction = 0
                rowIndex -= 1
        print('')

if __name__ == '__main__':
    grid = [[1, 2, 3, 4, 5, 6, 7, 8],
            [22, 23, 24, 25, 26, 27, 28, 9],
            [21, 36, 37, 38, 39, 40, 29, 10],
            [20, 35, 34, 33, 32, 31, 30, 11],
            [19, 18, 17, 16, 15, 14, 13, 12]]
    Solution().printSpiralTraversal(grid)
