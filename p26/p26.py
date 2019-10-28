class listNode:
    def __init__(self, value=0, nextNode=None):
        self.val = value
        self.next = nextNode

    def printList(self):
        while self.next:
            print(self.val, end=" -> ")
            self = self.next
        if self:
            print(self.val)
        else:
            print(None)

class Solution:
    def removeKthElementFromList(self, head, k):
        dummy = listNode(0, head)
        index1 = dummy
        index2 = dummy
        for _ in range(k):
            index2 = index2.next
        while index2.next:
            index1 = index1.next
            index2 = index2.next
        index1.next = index1.next.next
        return dummy.next

if __name__ == '__main__':
    n1 = listNode(15)
    n2 = listNode(5)
    n1.next = n2
    n3 = listNode(-3)
    n2.next = n3
    n4 = listNode(-3)
    n3.next = n4
    n5 = listNode(1)
    n4.next = n5
    n6 = listNode(6)
    n5.next = n6
    n7 = listNode(14)
    n6.next = n7
    n8 = listNode(7)
    n7.next = n8
    n9 = listNode(-7)
    n8.next = n9
    n10 = listNode(1)
    n9.next = n10

    head = n1
    head.printList()
    k = 5
    Solution().removeKthElementFromList(head, k).printList()
