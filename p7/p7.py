def sortNums(nums):
    ones = 0
    twos = 0
    threes = 0
    for mem in nums:
        if mem == 1:
            ones += 1
        elif mem == 2:
            twos += 1
        else:
            threes += 1
    for i in range(ones):
        nums[i] = 1
    for i in range(twos):
        nums[i + ones] = 2
    for i in range(threes):
       nums[i + ones + twos] = 3
    return nums

if __name__ == '__main__':
    print(sortNums([3, 2, 1, 3, 2, 1, 1, 1, 1, 1, 2, 3, 2, 1, 3, 2]))
