def longestSubsequence(lst):    # O(len(longest_subsequence) * n)
    maxLength = 0
    startIndex = 0
    endIndex = 0
    sequenceLength = len(lst)

    if sequenceLength == 0:
        maxLength = 0
        startIndex = 0
        endIndex = 0
    else:
        array = [[0] * sequenceLength for _ in range(sequenceLength)]
        for row in range(sequenceLength):
            element1 = lst[row]
            element2 = lst[row]
            array[row][row] = 1
            for column in range(row + 1, sequenceLength):
                if element2 == element1:
                    element2 = lst[column]
                if lst[column] != element1 and lst[column] != element2:
                    break
                else:
                    array[row][column] = array[row][column - 1] + 1
                    if array[row][column] > maxLength:
                        maxLength = array[row][column]
                        startIndex = row
                        endIndex = column
    return (startIndex, endIndex, maxLength)

def longestSubsequence2(lst):    # O(n)
    maxLength = 0
    dic = {}
    leftIndex = 0
    startIndex = 0
    endIndex = 0
    for index, element in enumerate(lst):
        dic[element] = index
        while len(dic) > 2:
            if dic[lst[leftIndex]] != dic[lst[index - 1]]:
                leftIndex = dic[lst[leftIndex]]
                del dic[lst[leftIndex]]
            leftIndex += 1
        currentLength = index - leftIndex + 1
        if maxLength < currentLength:
            maxLength = currentLength
            startIndex = leftIndex
            endIndex = index
    return (startIndex, endIndex, maxLength)

def printLongestSubsequence(lst, subsequenceInfoTuple):
    startIndex, endIndex, length = subsequenceInfoTuple
    print("The longest subsequence has length %d" % length)
    print("The sequence is:")
    print(lst[startIndex:endIndex + 1])

if __name__ == '__main__':
    lst = []
    printLongestSubsequence(lst, longestSubsequence2(lst))
    lst = [1, 3, 5, 3, 1, 3, 1, 5]
    printLongestSubsequence(lst, longestSubsequence2(lst))
    lst = [3, 3, 4, 3, 7, 6, 6, 2, 7, 7, 2, 7, 6]
    printLongestSubsequence(lst, longestSubsequence2(lst))
    lst = [3, 3, 4]
    printLongestSubsequence(lst, longestSubsequence2(lst))
    lst = [3, 2, 4, 4, 4, 2, 1, 2, 2, 1, 2]
    printLongestSubsequence(lst, longestSubsequence2(lst))
