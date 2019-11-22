class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []
        length = len(nums)
        for i in range(0, length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i + 1, length - 1
            while start < end:
                if nums[start] + nums[end] == -nums[i]:
                    triplets.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start - 1] == nums[start]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif nums[start] + nums[end] < -nums[i]:
                    start += 1
                else:
                    end -= 1

        return triplets

if __name__ == '__main__':
    nums = [0, -1, 2, -3, 1]
    print(Solution().threeSum(nums))
