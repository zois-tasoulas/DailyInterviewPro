from heapq import heappush, heappop

class Solution:
    def runningMedian(self, array):
        """
        :type array: List[int]
        :rtype: List[int]
        """
        answer = []
        low = []
        high = []
        length = len(array)
        if length == 0:
            pass
        elif length == 1:
            answer.append(array[0])
        else:
            answer.append(array[0])
            answer.append((array[0] + array[1]) / 2)
            heappush(low, -min(array[0], array[1]))
            heappush(high, max(array[0], array[1]))
            numsLow = 1
            numsHigh = 1
            for i in range(2, length):
                if array[i] < -low[0]:
                    heappush(low, -array[i])
                    numsLow += 1
                else:
                    heappush(high, array[i])
                    numsHigh += 1
                if numsLow - numsHigh == 2:
                    heappush(high, -heappop(low))
                    numsLow -= 1
                    numsHigh += 1
                elif numsLow - numsHigh == -2:
                    heappush(low, -heappop(high))
                    numsLow += 1
                    numsHigh -= 1
                if numsLow == numsHigh:
                    answer.append((-low[0] + high[0]) / 2)
                elif numsLow > numsHigh:
                    answer.append(-low[0])
                else:
                    answer.append(high[0])
                
        return answer

if __name__ == '__main__':
    lst = [1, 5, 6, 3, 15, 9, 8, 20, 12, 16, 7, 4]
    print(Solution().runningMedian(lst))
