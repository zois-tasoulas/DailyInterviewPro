class Solution:
    def getRange(self, arr, target):
        start = -1
        end = -1
        i = 0
        for num in arr:
            if num == target and start == -1:
                start = i
                end = i
            elif num == target:
                end = i
            i += 1
        return (start, end)

if __name__ == '__main__':
    arr = [1, 2, 2, 2, 3, 4, 8, 8]
    x = 2
    print(Solution().getRange(arr, x))
    arr = [1, 20, 30, 40, 50, 150]
    x = 150
    print(Solution().getRange(arr, x))
    arr = [10, 25, 26, 36, 39, 40, 41, 45, 68, 99]
    x = 42
    print(Solution().getRange(arr, x))
