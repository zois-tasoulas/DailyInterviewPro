class Solution:
    def numberRanges(self, lst):
        """
        :type lst: List[int]
        :rtype: List[str]
        """
        answer = []
        if lst:
            start = lst[0]
            prev = lst[0]
            for number in lst:
                if number > prev + 1:
                    answer.append(str(start) + "->" + str(prev))
                    start = number
                prev = number
            answer.append(str(start) + "->" + str(prev))
        return answer

if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1, 1, 3, 4, 5, 5, 5, 9, 15, 16, 18, 19, 20, 21]
    print(Solution().numberRanges(numbers))
