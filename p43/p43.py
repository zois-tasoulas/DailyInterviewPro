class Solution:
    def smallestMissing(self, array):
        length = len(array)
        for i in range(length):
            while 0 < array[i] <= length and array[array[i] - 1] != array[i]:
                aux = array[i] - 1
                array[i], array[aux] = array[aux], array[i]
        for i in range(length):
            if array[i] != i + 1:
                return i + 1 
        return length + 1

if __name__ == '__main__':
    lst = [3, 4, -2, 7, -3, 1, 15, 2, 29, 14, 15, 6, 9]
    print(Solution().smallestMissing(lst))
