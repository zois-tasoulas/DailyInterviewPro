class TreeNode:
    def __init__(self, value, left=None, right=None):
        """
        :type value: int, left: TreeNode, right: TreeNode
        """
        self.val = value
        self.left = left
        self.right = right

    def printInorder(self):
        if self:
            if self.left:
                self.left.printInorder()
            print(self.val)
            if self.right:
                self.right.printInorder()

class Solution:
    def findLargestBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        BSTRoot, _ = self.findBST(root)
        return BSTRoot

    def findBST(self, root):
        """
        :type root: TreeNode
        :rtype: (TreeNode, int)
        """
        if not root:
            return (None, 0)
        elif root.left and root.right:
            leftBST = self.findBST(root.left)
            rightBST = self.findBST(root.right)
            if root.left.val <= root.val and root.right.val >= root.val and leftBST[0] is root.left and rightBST[0] is root.right:
                return (root, leftBST[1] + rightBST[1] + 1)
            else:
                return leftBST if leftBST[1] >= rightBST[1] else rightBST
        elif root.left:
            leftBST = self.findBST(root.left)
            if root.left.val <= root.val and leftBST[0] is root.left:
                return (root, leftBST[1] + 1)
            else:
                return leftBST
        elif root.right:
            rightBST = self.findBST(root.right)
            if root.right.val >= root.val and rightBST[0] is root.right:
                return (root, rightBST[1] + 1)
            else:
                return rightBST
        else:
            return (root, 1)
        
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(16)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(6)
    root.left.right.left.left = TreeNode(3)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(29)
    root.right.right.left = TreeNode(25)
    root.right.right.right = TreeNode(42)

    rootBST = Solution().findLargestBST(root)
    rootBST.printInorder()
