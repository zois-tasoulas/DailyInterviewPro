class Solution:
    def distributeBonuses(self, perf):
        """
        :type perf: List[int]
        :rtype: List[int]
        """
        bonuses = [1 for _ in range(len(perf))]
        for index in range(1, len(perf)):
            if perf[index] > perf[index - 1]:
                bonuses[index] = 2
            elif perf[index] < perf[index - 1]:
                bonuses[index - 1] += 1
        return bonuses

if __name__ == '__main__':
    employPerformance = [17, 5, 17, 18, 3, 67]
    print(Solution().distributeBonuses(employPerformance))
