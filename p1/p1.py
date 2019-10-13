class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        if l1 is None and l2 is None:
            if c == 1:
                return ListNode(1)
            else:
                return None
        elif l1 is None:
            aux = l2.val + c
            myNode = ListNode(aux % 10)
            myNode.next = self.addTwoNumbers(None, l2.next, aux / 10)
            return myNode
        elif l2 is None:
            aux = l1.val + c
            myNode = ListNode(aux % 10)
            myNode.next = self.addTwoNumbers(l1.next, None, aux / 10)
            return myNode
        else:
            aux = l1.val + l2.val + c
            myNode = ListNode(aux % 10)
            myNode.next = self.addTwoNumbers(l1.next, l2.next, aux / 10)
            return myNode

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.next.next.next = ListNode(8)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next
