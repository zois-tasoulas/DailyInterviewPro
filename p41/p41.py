from collections import defaultdict

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def deepestNode(self, root):
        if not root:
            return (None, 0)
        level = 1
        maxTuple = (root.val, 1)
        stack = []
        explored = defaultdict(int)     #Default value for int is 0
        stack.append((root, level))
        while stack:
            currentTuple = stack.pop()
            if explored[currentTuple[0]] == 1:
                continue
            explored[currentTuple[0]] = 1
            if currentTuple[1] > maxTuple[1]:
                maxTuple = currentTuple
            if currentTuple[0].right:
                stack.append((currentTuple[0].right, currentTuple[1] + 1))
            if currentTuple[0].left:
                stack.append((currentTuple[0].left, currentTuple[1] + 1))
            
        return maxTuple[0].val, maxTuple[1]

if __name__ == '__main__':
    root = TreeNode('a')
    root.left = TreeNode('b', TreeNode('d'), TreeNode('g'))
    root.right = TreeNode('c')
    root.right.right = TreeNode('e')
    root.right.right.right = TreeNode('f', TreeNode('h'), root.left)
    print(Solution().deepestNode(root))
