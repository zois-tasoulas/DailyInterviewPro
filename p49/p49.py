class Solution:
    def sortColors(self, array):
        nextRed = 0
        nextBlue = len(array) - 1
        index = 0
        while index <= nextBlue:
            if array[index] == 0:
                swap(array, nextRed, index)
                nextRed += 1
                index += 1
            elif array[index] == 2:
                swap(array, nextBlue, index)
                nextBlue -= 1
            else:
                index += 1

def swap(lst, a, b):
    lst[b], lst[a] = lst[a], lst[b]

if __name__ == '__main__':
    lst = [2, 2, 2, 2, 0, 0, 1, 0, 2, 0, 1, 0, 2, 1]
    Solution().sortColors(lst)
    print(lst)
