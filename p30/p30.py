def createHeap(heap, numOfElements):
    for i in range(k - 1, 0, -1):    #heapify only the first half of the elements
        heapify(i, heap)

def heapify(index, heap):            #fill out this one
    if heap[index] > heap[] and heap[] > heap[]:
        swap()
        heapify(, heap)
    elif heap[index] > heap[]:
        swap()
        heapify(, heap)
    elif heap[index] > heap[]:
        swap()
        heapify(, heap)

class Solution:
    def kLargestElement(self, lst, k):
        minHeap = lst[:k]
        createHeap(minHeap, k)
        for i in range(k, len(lst)):
            if lst[i] > minHeap[0]:
                minHeap[0] = lst[i]
                heapify(0, minHeap)

        return minHeap[0]

if __name__ == '__main__':
    lst = [3, 5, 2, 4, 6, 8]
    k = 3
    print(Solution().kLargestElement(lst, k))
