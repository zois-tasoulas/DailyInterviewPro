class Solution:
    def moveZeros(self, array):
        positionsToMove = 0
        for i in range(len(array)):
            if array[i] == 0:
                positionsToMove += 1
            elif positionsToMove > 0:
                array[i - positionsToMove] = array[i]
                array[i] = 0

if __name__ == '__main__':
    array = [1, 0, 2, 0, 5, 3, 4, 0]
    Solution().moveZeros(array)
    print(array)
