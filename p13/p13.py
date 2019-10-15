def maxOf(num1, num2):
    if num1 > num2:
        return num1
    return num2

class stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if self.stack:
            (a, prevMax) = self.stack[-1]
        else:
            prevMax = val
        self.stack.append((val, maxOf(prevMax, val)))

    def pop(self):
        if self.stack:
            (val, b) = self.stack[-1]
            self.stack.pop()
            return val
        return None

    def max(self):
        if self.stack:
            (a, mxm) = self.stack[-1]
            return mxm
        return None

if __name__ == '__main__':
    s = stack()
    s.push(8)
    s.push(42)
    s.push(7)
    s.push(58)
    s.push(5)
    print(s.max())
    retElem = s.pop()
    print(s.max())
    retElem = s.pop()
    retElem = s.pop()
    retElem = s.pop()
    print(s.max())
    retElem = s.pop()
    print(s.max())
