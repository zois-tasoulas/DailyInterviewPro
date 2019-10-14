class myStack:
    def __init__(self, aList = None):
        if aList is None:
            aList = []
        self.lst = aList

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def isEmpty(self):
        return self.lst == []

class Solution:
    def isValid(self, s):
        stack = myStack()
        for char in s:
             if char == '(' or char == '[' or char == '{':
                 stack.push(char)
             elif char == ')':
                 if stack.pop() != '(':
                     return False
             elif char == ']':
                 if stack.pop() != '[':
                     return False
             elif char == '}':
                 if stack.pop() != '{':
                     return False
                 
        return stack.isEmpty()

if __name__ == '__main__':
    s = "()(){(())"
    print(Solution().isValid(s))
    s = ""
    print(Solution().isValid(s))
    s = "([{}])()"
    print(Solution().isValid(s))
    s = "(((([{}]))))()[]{}{[](){}]"
    print(Solution().isValid(s))
