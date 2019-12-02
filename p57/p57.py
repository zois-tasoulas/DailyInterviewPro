from heapq import heappush, heappop

class Solution:
    def roomScheduling(self, classes):
        """
        :type classes: List[(int, int)]
        :rtype: int
        """
        maxRooms = 0
        rooms = 0
        heap = []
        classes.sort()
        for start, end in classes:
            while heap and heap[0] <= start:
                heappop(heap)
                rooms -= 1
            heappush(heap, end)
            rooms += 1
            maxRooms = max(maxRooms, rooms)
        return maxRooms

if __name__ == '__main__':
    classes = [(30, 75), (0, 50), (60, 150), (125, 140), (90, 140), (75, 100), (60, 120)]
    print(Solution().roomScheduling(classes))
