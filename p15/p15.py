def pythagoreanTriplets(lst):
    length = len(lst)
    for i in range(length):
        lst[i] = lst[i]**2
    squareSet = set(lst)
    for i in range(length - 1):
        for j in range(i, length):
            if (lst[i] + lst[j]) in squareSet:
                return True
    return False

if __name__ == '__main__':
    lst = [2, 1, 11, 13, 4, 42, 55, 8, 66, 7, 11, 5, 3]
    print(pythagoreanTriplets(lst))
