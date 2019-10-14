class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    def reverseRecursively(self, head):
        self.recursion()
        head.next = None

    def recursion(self):
        if self.next is None:
            pass
        else:
            self.next.recursion()
            self.next.next = self

    def reverseIteratively(self, head):
        node = head
        nextNode = head.next
        aux = head.next
        while nextNode is not None:
            aux = nextNode
            nextNode = nextNode.next
            aux.next = node
            node = aux
        head.next = None

if __name__ == '__main__':
    testHead = ListNode(1)
    node1 = ListNode(9)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(9)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(3)
    node4.next = node5
    testTail = ListNode(8)
    node5.next = testTail
 
    print("Initial list: ")
    testHead.printList()
    testHead.reverseIteratively(testHead)
    print("List after reversal (iteratively): ")
    testTail.printList()
    testHead.reverseIteratively(testTail)
    testHead.reverseRecursively(testHead)
    print("List after reversal (recursively): ")
    testTail.printList()
