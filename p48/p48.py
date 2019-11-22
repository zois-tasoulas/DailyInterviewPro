class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def printTreeInorder(self):
        if self.left:
            self.left.printTreeInorder()
        if self:
            print(self.val)
        if self.right:
            self.right.printTreeInorder()

class Solution:
    def reconstructTree(self, preorder, inorder):
        if not preorder:
            return None
        return self.createTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def createTree(self, preorder, preFirst, preLast, inorder, inFirst, inLast):
        root = TreeNode(preorder[preFirst])
        if inFirst != inLast:
            cnt = 0
            for i in range(inFirst, inLast + 1):
                if inorder[i] == preorder[preFirst]:
                    break
                cnt += 1
            if preFirst + 1 <= preFirst + cnt:
                root.left = self.createTree(preorder, preFirst + 1, preFirst + cnt,
                                            inorder, inFirst, inFirst + cnt - 1)
            if preFirst + cnt + 1 <= preLast:
                root.right = self.createTree(preorder, preFirst + cnt + 1, preLast,
                                             inorder, inFirst + cnt + 1, inLast)
        return root

if __name__ == '__main__':
    preorder = ['a', 'b', 'c', 'd', 'e']
    inorder = ['b', 'a', 'd', 'c', 'e']
    root = Solution().reconstructTree(preorder, inorder)
    root.printTreeInorder()
