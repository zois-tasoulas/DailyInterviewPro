def check(lst):
    prevElem = lst[0]
    change = 0
    for num in lst[1:]:
        if prevElem > num:
            change += 1
            if change > 1:
                return False
        prevElem = num
    return True

if __name__ == '__main__':
    print(check([2, 4, 7, 7, 5, 7, 14, 23]))
    print(check([5, 5, 6, 7, 6, 9, 13, 65, 42]))
