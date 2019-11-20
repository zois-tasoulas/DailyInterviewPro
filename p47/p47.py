class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def univalSubtrees(self, root):
        if not root:
            return 0
        if root.left and root.right:
            if root.left.val == root.val and root.right.val == root.val:
                return 1 + self.univalSubtrees(root.left) + self.univalSubtrees(root.right)
            else:
                return self.univalSubtrees(root.left) + self.univalSubtrees(root.right)
        elif root.left:
            if root.left.val == root.val:
                return 1 + self.univalSubtrees(root.left)
            else:
                return self.univalSubtrees(root.left)
        elif root.right:
            if root.right.val == root.val:
                return 1 + self.univalSubtrees(root.right)
            else:
                return self.univalSubtrees(root.right)
        else:
            return 1

if __name__ == '__main__':
    root = TreeNode(0, TreeNode(1), TreeNode(0, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(0)))
    print(Solution().univalSubtrees(root))
