class Solution:
    def longestIncreasingSubsequence(self, array):
        """
        :type array: List[int]
        :rtype: int
        """
        if not array:
            return 0
        dp = [1]
        answer = 1
        for i in range(1, len(array)):
            maxLIS = 1
            for j in range(0, i):
                if array[i] > array[j] and dp[j] + 1 > maxLIS:
                    maxLIS = dp[j] + 1
            dp.append(maxLIS)
            answer = max(answer, maxLIS)
        return answer

    # NlogN
    def LIS(self, array):
        """
        :type array: List[int]
        :rtype: int
        """
        def binarySearch(nums, start, end, element):
            median = start + (end - start) // 2
            if nums[median] >= element:
                if median == start or nums[median - 1] < element:
                    return median
                else:
                    return binarySearch(nums, start, median - 1, element)
            else:
                return binarySearch(nums, median + 1, end, element)

        tails = []
        for num in array:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                pos = binarySearch(tails, 0, len(tails) - 1, num)
                tails[pos] = num
        return len(tails)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().longestIncreasingSubsequence(nums))
    print(Solution().LIS(nums))
