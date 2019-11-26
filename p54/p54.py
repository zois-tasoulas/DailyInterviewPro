class Solution:
    def numberOfParenthesis(self, string):
        """
        :type: String
        :rtype: int
        """
        stack = []
        misplaced = 0
        for char in string:
            if char == '(':
                stack.append('(')
            else:
                if stack and stack[-1] == '(':
                        stack.pop()
                else:
                    misplaced += 1
        while stack:
            stack.pop()
            misplaced += 1

        return misplaced

if __name__ == '__main__':
    parenthesis = "())()((()())"
    print(Solution().numberOfParenthesis(parenthesis))
