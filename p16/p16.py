def distanceCalculator(str1, str2):
    lengthString1 = len(str1)
    lengthString2 = len(str2)
    array = [[0] * (lengthString2 + 1) for i in range(lengthString1 + 1)]

    for i in range(lengthString1 + 1):
        array[i][0] = i
    for j in range(lengthString2 + 1):
        array[0][j] = j
    for i in range(1, lengthString1 + 1):
        for j in range(1, lengthString2 + 1):
            if str1[i - 1] == str2[j - 1]:
                difference = 0
            else:
                difference = 1
            array[i][j] = min( array[i][j - 1] + 1, array[i -1 ][j] + 1, array[i - 1][j - 1] + difference)
    return array[lengthString1][lengthString2]

if __name__ == '__main__':
    str1 = "banana"
    str2 = "anaxnac"
    print(distanceCalculator(str1, str2))
