class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def valuesInHeight(self, root, h):
        queue = []
        answer = []
        if root:
            queue.append((root, 1))
        while queue:
            level = queue[0][1]
            '''
            If we are visiting the nodes at h we do not
            need to append their children to the queue
            '''
            if level == h:    
                answer.append(queue[0][0].val)
            else:
                if queue[0][0].left:
                    queue.append((queue[0][0].left, level + 1))
                if queue[0][0].right:
                    queue.append((queue[0][0].right, level + 1))
            del queue[0]

        return answer 

if __name__ == '__main__':
    h = 3
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.right.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(8)
    root.left.left.left = TreeNode(7)
    print(Solution().valuesInHeight(root, h))
