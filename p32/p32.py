class Solution:
    def largestProduct(self, lst):
        maxNums = [0 for _ in range(3)]
        minNums = [0 for _ in range(2)]
        maxNums[2] = max(lst[0], lst[1], lst[2])
        minNums[1] = min(lst[0], lst[1], lst[2])
        if maxNums[2] == lst[0]:
            maxNums[1] = max(lst[1], lst[2])
            maxNums[0] = min(lst[1], lst[2])
            minNums[0] = max(lst[1], lst[2])
        elif maxNums[2] == lst[1]:
            maxNums[1] = max(lst[0], lst[2])
            maxNums[0] = min(lst[0], lst[2])
            minNums[0] = max(lst[0], lst[2])
        else:
            maxNums[1] = max(lst[0], lst[1])
            maxNums[0] = min(lst[0], lst[1])
            minNums[0] = max(lst[0], lst[1])
        for i in range(3, len(lst)):
            if lst[i] > maxNums[2]:
                maxNums[0] = maxNums[1]
                maxNums[1] = maxNums[2]
                maxNums[2] = lst[i]
            elif lst[i] > maxNums[1]:
                maxNums[0] = maxNums[1]
                maxNums[1] = lst[i]
            elif lst[i] > maxNums[0]:
                maxNums[0] = lst[i]
            if lst[i] < minNums[1]:
                minNums[0] = minNums[1]
                minNums[1] = lst[i]
            elif lst[i] < minNums[0]:
                minNums[0] = lst[i]
        return max(maxNums[0] * maxNums[1] * maxNums[2], maxNums[2] * minNums[0] * minNums[1])

if __name__ == '__main__':
    lst = [1, 2, 3, -2, -3]
    #lst = [-4, -4, 2, 8]
    #lst = [-4, -4, -2, -8]
    print(Solution().largestProduct(lst))
