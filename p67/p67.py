class Solution:
    def minimumUnsortedRange(self, lst):
        """
        :type lst: [int]
        :rtype: (int, int)
        """
        if len(lst) < 2:
            return None
        left = -1
        right = len(lst)
        for index in range(1, len(lst)):
            if lst[index] < lst[index - 1]:
                left = index - 1
                break
        for index in range(len(lst) - 2, -1, -1):
            if lst[index] > lst[index + 1]:
                right = index + 1
                break
        minim = min(lst[left:])
        maxim = max(lst[:right])
        for index in range(0, left):
            if minim < lst[index]:
                left = index
                break
        for index in range(len(lst) - 1, right, -1):
            if maxim > lst[index]:
                right = index
                break
        return (left, right) if left != -1 else None

if __name__ == '__main__':
    lst = [1, 2, 4, 5, 15, 12, 20, 21, 22]
    print(Solution().minimumUnsortedRange(lst))
