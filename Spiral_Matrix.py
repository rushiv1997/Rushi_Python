def SpiralMatrix(test, i, j, m, n):
    # If i or j lies outside the matrix
    if (i >= m or j >= n):
        return
    # Print First Row
    for p in range(i, n):
        print(test[i][p], end=" ")
    # Print Last Column
    for p in range(i + 1, m):
        print(test[p][n - 1], end=" ")
    # Print Last Row, if Last and First Row are not same
    if ((m - 1) != i):
        for p in range(n - 2, j - 1, -1):
            print(test[m - 1][p], end=" ")
    # Print First Column, if Last and First Column are not same
    if ((n - 1) != j):
        for p in range(m - 2, i, -1):
            print(test[p][j], end=" ")
    SpiralMatrix(test, i + 1, j + 1, m - 1, n - 1)

if __name__ == "__main__":
    R = 4
    C = 4
    test = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    SpiralMatrix(test, 0, 0, R, C)
