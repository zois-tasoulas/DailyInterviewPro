def two_sum(lst, k):
    d = {}
    for num in lst:
        if k - num in d:
            return True
        d[num] = 1
    return False

if __name__ == '__main__':
    print(two_sum([4, 7, 1, -3, 2], 5))
    print(two_sum([4, 2, 1, -3, 2, 15, 10], 4))
