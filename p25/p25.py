class listNode:
    def __init__(self, value=0, nextNode=None):
        self.value = value
        self.next = nextNode

    def printList(self):
        if self is None:
            print(self)
        else:
            while self.next:
                print("%d" % self.value, end=" -> ")
                self = self.next
            print("%d" % self.value)

def removeConsecutiveSumTo0(head):
    dummy = listNode(0)
    dummy.next = head
    prefixSum = 0
    d = {0:dummy}
    while head:
        prefixSum += head.value
        d[prefixSum] = head
        head = head.next
    head = dummy
    prefixSum = head.value
    while head:
        prefixSum += head.value
        head.next = d[prefixSum].next
        head = head.next

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
    removeConsecutiveSumTo0(head).printList()
