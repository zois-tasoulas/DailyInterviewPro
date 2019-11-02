def swap(index1, index2, array):
    c = array[index1]
    array[index1] = array[index2]
    array[index2] = c

def createHeap(heap, numOfElements):
    for i in range(numOfElements // 2 - 1, -1, -1):
        heapify(i, numOfElements, heap)

def heapify(index, numOfElements, heap):
    if index > numOfElements // 2 - 1:
        pass
    else:
        if (index + 1) * 2 < numOfElements :
            if heap[index] > heap[(index + 1) * 2] and heap[(index + 1) * 2] > heap[(index + 1) * 2 - 1]:
                swap(index, (index + 1) * 2 - 1, heap)
                heapify((index + 1) * 2 - 1, numOfElements, heap)
            elif heap[index] > heap[(index + 1) * 2]:
                swap(index, (index + 1) * 2, heap)
                heapify((index + 1) * 2, numOfElements, heap)
            elif heap[index] > heap[(index + 1) * 2 - 1]:
                swap(index, (index + 1) * 2 - 1, heap)
                heapify((index +1) * 2 - 1, numOfElements, heap)
        elif heap[index] > heap[(index + 1) * 2 - 1]:
            swap(index, (index + 1) * 2 - 1, heap)
            heapify((index +1) * 2 - 1, numOfElements, heap)

class Solution:
    def kLargestElement(self, lst, k):
        minHeap = lst[:k]
        createHeap(minHeap, k)
        for i in range(k, len(lst)):
            if lst[i] > minHeap[0]:
                minHeap[0] = lst[i]
                heapify(0, k, minHeap)

        return minHeap[0]

if __name__ == '__main__':
    lst = [5, 8, 8, 15, 5, 3, 9, 7, 9, 11, 2, 13]
    k = 4
    print(Solution().kLargestElement(lst, k))
