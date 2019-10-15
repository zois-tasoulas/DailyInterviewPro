''' n must be at least 1'''
def staircase(n):
    array = [1, 2]
    for i in range(2, n):
        array.append(array[i - 2] + array[i - 1])
    return array[n - 1]

if __name__ == '__main__':
    print(staircase(4))
    print(staircase(5))
    print(staircase(15))
