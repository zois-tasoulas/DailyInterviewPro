class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        acc = nums[0]
        answer.append(1)
        for i in range(1, len(nums)):
            answer.append(acc)
            acc *= nums[i]
        acc = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= acc
            acc *= nums[i]
        return answer

if __name__ == '__main__':
    numbers = [5, 2, 3, 1, 4]
    print(Solution().productExceptSelf(numbers))
