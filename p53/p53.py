class Solution:
    def countIslands(self, landscape):
        """
        :type landscape: List[List[int]]
        :rtype: int
        """
        if not landscape:
            return 0
        numOfLines = len(landscape)
        numOfColumns = len(landscape[0]) 
        numOfIslands = 0
        for i in range(numOfLines):
            for j in range(numOfColumns):
                if landscape[i][j] == 1:
                    numOfIslands += 1
                    self.eraseIsland(landscape, i, j, numOfLines, numOfColumns)
        return numOfIslands

    def eraseIsland(self, landscape, x, y, xBorder, yBorder):
        """
        :type landscape: List[List[int]], x: int, y: int, xBorder: int, yBorder: int
        :rtype: None
        """
        landscape[x][y] = 0
        if x + 1 < xBorder and landscape[x + 1][y] == 1:
            self.eraseIsland(landscape, x + 1, y, xBorder, yBorder)
        if x - 1 >= 0 and landscape[x - 1][y] == 1:
            self.eraseIsland(landscape, x - 1, y, xBorder, yBorder)
        if y + 1 < yBorder and landscape[x][y + 1] == 1:
            self.eraseIsland(landscape, x, y + 1, xBorder, yBorder)
        if y - 1 >= 0 and landscape[x][y - 1] == 1:
            self.eraseIsland(landscape, x, y - 1, xBorder, yBorder)

if __name__ == '__main__':
    landscape = [[1, 1, 1], [0, 1, 0],
                 [1, 1, 1]]
    print(Solution().countIslands(landscape))
