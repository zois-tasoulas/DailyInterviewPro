class TreeNode:
    def __init__(self, value, left=None, right=None):
        """
        :type value: char, left: TreeNode, right: TreeNode
        """
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def calculateExpression(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            left = self.calculateExpression(root.left)
        else:
            left = 0    #Allow unary operators
        if root.right:
            right = self.calculateExpression(root.right)
        else:
            right = 0    #Allow unary operators
        if root.val == '+':
            return left + right
        elif root.val == '-':
            return left - right
        elif root.val == '*':
            return left * right
        elif root.val == '/':
            return left // right
        else:
            return int(root.val)

if __name__ == '__main__':
    root = TreeNode('*')
    root.left = TreeNode('-')
    root.left.left = TreeNode('+', TreeNode('3'), TreeNode('5'))
    root.left.right = TreeNode('2')
    root.right = TreeNode('-', None, TreeNode('6'))
    print(Solution().calculateExpression(root))
