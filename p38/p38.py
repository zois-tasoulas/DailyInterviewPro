class TreeNode:
    def __init__(self, value, leftChild=None, rightChild=None):
        self.val = value
        if leftChild is None:
            leftChild = []
        if rightChild is None:
            rightChild = []
        self.left = leftChild
        self.right = rightChild

    def printTree(self):
        self.printNodes()
        print()

    def printNodes(self):
        if not self:
            print("Print called on an empty tree")
        print(self.val, end=' ')
        if self.left:
            self.left.printNodes()
        if self.right:
            self.right.printNodes()

class Solution:
    def createTreeFromList(self, lst):
        root = None
        if lst:
            root = self.createTree(lst, 0, len(lst) - 1)

        return root

    def createTree(self, lst, startIndex, endIndex):
        middle = startIndex + (1 + endIndex - startIndex) // 2
        root = TreeNode(lst[middle])
        if endIndex - startIndex > 0:
            root.left = self.createTree(lst, startIndex, middle - 1)
            if endIndex - startIndex > 1:
                root.right = self.createTree(lst, middle + 1, endIndex)

        return root

if __name__ == '__main__':
    lst = [1, 2, 3, 15, 16, 17, 19, 68, 152]
    Solution().createTreeFromList(lst).printTree()
