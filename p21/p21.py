def minimalSubarray(lst, s):
    leftIndex = 0
    arrayLength = len(lst)
    minSubarray = arrayLength + 1
    currentSum = 0
    for rightIndex, element in enumerate(lst):
        currentSum += element
        if currentSum > s:
            while currentSum > s and leftIndex <= rightIndex:
                currentSum -= lst[leftIndex]
                leftIndex += 1
        if currentSum == s and rightIndex - leftIndex + 1 < minSubarray:
            minSubarray = rightIndex - leftIndex + 1
        if minSubarray == 1:	#A subarray of one element is the shortest possible subarray
            break

    return minSubarray if minSubarray <= arrayLength else 0

if __name__ == '__main__':
    array = [2, 3, 1, 3, 4, 9, 5, 4, 3, 2, 7, 6, 1, 3, 15, 4, 4, 1, 4, 42, 5]
    s = 9
    print(minimalSubarray(array, s))
    s = 44
    print(minimalSubarray(array, s))
    s = 39
    print(minimalSubarray(array, s))
