class listNode:
    def __init__(self, number=0, nextNode=None):
        self.id = number
        self.next = nextNode

    def printList(self):
        while self:
            print(self.id)
            self = self.next

    def length(self):
        lngth = 0
        while self:
            lngth += 1
            self = self.next
        return lngth

def findIntersection(list1, list2):
    d = {}
    while list1:
        d[list1.id] = True
        list1 = list1.next
    while list2:
        if list2.id in d:
            return list2
        list2 = list2.next

def findIntersection2(list1, list2):    #Constant memory version
    length1 = list1.length()
    length2 = list2.length()

    if length1 < length2:
        for i in range(length2 - length1):
            list2 = list2.next
    else:
        for i in range(length1 - length2):
            list1 = list1.next
    while list1 and list2:
        list1 = list1.next
        list2 = list2.next
        if list1 == list2:
            break
    return list1 if list1 == list2 else None

if __name__ == '__main__':
    l1 = listNode(11)
    l1.next = listNode(7)
    l1.next.next = listNode(2)
    l1.next.next.next = listNode(5)
    l1.next.next.next.next = listNode(13)
    l2 = listNode(4)
    l2.next = l1.next.next.next

    node = findIntersection2(l1, l2)
    if node:
        node.printList()
    else:
        print(None)
