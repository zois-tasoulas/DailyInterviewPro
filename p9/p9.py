def singleNumber(nums):
    a = 0
    for mem in nums:
        a = a ^ mem    #a XOR a = 0, a XOR 0 = a
    return a

if __name__ == '__main__':
    print(singleNumber([4, 9, 2, 4, 11, 2, 9]))
    print(singleNumber([8, 13, 27, 27, 87, 42, 13, 8, 87]))
