class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def validateBST(self, root):

        return self.validateNode(root, float('-inf'), float('inf'))

    def validateNode(self, root, lowerLimit, upperLimit):
        if not root:
            return True
        if root.val < lowerLimit or root.val > upperLimit:
            return False
        else:
            return self.validateNode(root.left, lowerLimit, root.val) and self.validateNode(root.right, root.val, upperLimit)
    
if __name__ == '__main__':
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4, TreeNode(3), TreeNode(4))), TreeNode(10))
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(20)
    print(Solution().validateBST(root))
