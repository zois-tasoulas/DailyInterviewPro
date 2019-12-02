class Solution:
    def intersection(self, array1, array2):
        """
        :type array1: List[int], array2: List[int]
        :rtype: List[int]
        """
        return list(set(array1) & set(array2))

if __name__ == '__main__':
    lst1 = [2, 9, 5, 2, 5, 6, 6, 6]
    lst2 = [8, 7, 6, 5, 4]
    print(Solution().intersection(lst1, lst2))
