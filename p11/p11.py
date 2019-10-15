class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def solution(self, k):
        return (self.findFloor(k), self.findCeiling(k))

    def findFloor(self, k):
        if self.value == k:
            return k
        elif self.value > k:
            if self.left is None:
                return None
            return self.left.findFloor(k)
        else:
            if self.right is None:
                return self.value
            potFloor = self.right.findFloor(k)
            if potFloor > self.value:
                return potFloor
            return self.value

    def findCeiling(self, k):
        if self.value == k:
            return k
        elif self.value < k:
            if self.right is None:
                return None
            return self.right.findCeiling(k)
        else:
            if self.left is None:
                return self.value
            potCeiling = self.left.findCeiling(k)
            if potCeiling is not None and potCeiling < self.value:
                return potCeiling
            return self.value

if __name__ == '__main__':
    root = treeNode(11, treeNode(4), treeNode(16))
    root.left.left = treeNode(2, treeNode(1))
    root.left.right = treeNode(6, None, treeNode(9))
    root.right.left = treeNode(14, treeNode(13), treeNode(15))
    root.right.right = treeNode(25, None, treeNode(42))

    k = 10
    print(root.solution(k))
    k = 65
    print(root.solution(k))
    k = 13
    print(root.solution(k))
    k = 8
    print(root.solution(k))
