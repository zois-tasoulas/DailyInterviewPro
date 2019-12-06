class TreeNode:
    def __init__(self, value, left=None, right=None):
        """
        :type value: int or str, left: TreeNode, right: TreeNode
        """
        self.val = value
        self.left = left
        self.right = right

    def __str__(self):
        """
        :rtype: str
        """
        preOrder = ""
        if self:
            preOrder += str(self.val)
        if self.left:
            preOrder += " " + str(self.left)
        if self.right:
            preOrder += " " + str(self.right)
        return preOrder

class Solution:
    def serialize(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root:
            s = str(root.val) + " " \
                + self.serialize(root.left) + " " \
                + self.serialize(root.right)
        else:
            s = "#"
        return s

    def deserialize(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        lst = s.split()
        if lst[0] == "#":
            return None
        root = TreeNode(lst[0])
        prev = root
        nextRight = [root]
        goRight = False
        for index in range(1, len(lst)):
            if lst[index] == "#":
                if nextRight:  # Neccesary for the last '#' of the string
                    prev = nextRight.pop()
                goRight = True
            else:
                if goRight:
                    prev.right = TreeNode(lst[index])
                    prev = prev.right
                    goRight = False
                else:
                    prev.left = TreeNode(lst[index])
                    prev = prev.left
                nextRight.append(prev)
        return root

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(42, TreeNode(2), TreeNode(7))
    root.right = TreeNode(13)
    root.right.right = TreeNode(12, TreeNode(92))
    string = Solution().serialize(root)
    print(string)
    print(Solution().deserialize(string))
