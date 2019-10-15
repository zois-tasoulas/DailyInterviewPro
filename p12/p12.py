class treeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def reorderInPlace(self):
        if self.left:
            self.left.reorderInPlace()
        if self.right:
            self.right.reorderInPlace()
        aux = self.right
        self.right = self.left
        self.left = aux

if __name__ == '__main__':
    root = treeNode('a')
    root.left = treeNode('b', treeNode('d'), treeNode('e'))
    root.right = treeNode('c')
    root.right.right = treeNode('f', treeNode('g'), treeNode('h'))

    print("Initial tree")
    root.preorder() 
    print('\n')
    root.reorderInPlace()
    print("Tree after reordering")
    root.preorder()
