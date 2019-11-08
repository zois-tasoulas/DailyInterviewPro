from heapq import heappop, heapreplace, heapify

class List:
    '''
        __eq__ and __lt__ methods are needed for
        heapreplace.
        Apparently, if two tuples have equal first elements,
        Python3 will move on to compare the second elements
        of the tuples, in order to determine the order of
        the heap elements.
        If __eq__ and __lt__ do not exist, Python3 will
        raise an exception.
    '''
    def __init__(self, value, nextNode=None):
        self.data = value
        self.next = nextNode

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.data < other.data
        return NotImplemented

    def printList(self):
        while self:
            print(self.data, end=' ')
            self = self.next
        print()

class Solution:
    def mergeListsSlow(self, array):
        indexArray = []
        for member in array:
            indexArray.append(member)
        head = List(0)
        current = head
        minIndex = 0
        while minIndex > -1:
            minIndex = -1
            for i, node in enumerate(indexArray):
                if node:
                    if minIndex == -1:
                        minIndex = i
                    else:
                        if node.data < indexArray[minIndex].data:
                            minIndex = i
            if minIndex > -1:
                current.next = indexArray[minIndex]
                current = current.next
                indexArray[minIndex] = indexArray[minIndex].next
        return head.next

    def mergeLists(self, array):
        heap = []
        for member in array:
            if member:
                heap.append((member.data, member))
        heapify(heap)
        head = List(0)
        current = head
        while heap:
            if heap[0][1].next:
                _, current.next = heapreplace(heap, (heap[0][1].next.data, heap[0][1].next))
                current = current.next
            else:
                _, current.next = heappop(heap)
                current = current.next
        return head.next

if __name__ == '__main__':
    array = []
    head1 = List(1, List(5, List(9, List(13))))
    array.append(head1)
    head2 = List(-2, List(6, List(10)))
    array.append(head2)
    head3 = List(3, List(7))
    array.append(head3)
    head4 = List(4, List(8, List(12, List(16))))
    array.append(head4)
    head5 = List(3, List(6, List(13, List(15, List(17)))))
    array.append(head5)
    head6 = List(13)
    array.append(head6)
    head7 = None
    array.append(head7)
    Solution().mergeLists(array).printList()
