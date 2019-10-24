def gridTraversal(n, m):
    grid = [[0] * m] * n

    for i in range(n):
        grid[i][0] = 1
    for i in range(m):
        grid[0][i] = 1
    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

    return grid[n - 1][m - 1]

if __name__ == '__main__':
    n = 4
    m = 5
    print(gridTraversal(n, m))
