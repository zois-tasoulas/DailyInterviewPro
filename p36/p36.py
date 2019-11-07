class Solution:
    def maxSubarraySum(self, array):
        if not array:
            return None
        maxSum = array[0]
        currentSum = 0
        for member in array:
            currentSum += member
            maxSum = max(maxSum, currentSum)
            currentSum = max(0, currentSum)
        return maxSum

if __name__ == '__main__':
    lst = [1, 3, -2, 5, 7, 4, -12, -6, 15]
    print(Solution().maxSubarraySum(lst))
