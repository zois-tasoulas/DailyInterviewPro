class Solution:
    def mergeIntervals(self, intervals):
        minStart = intervals[0][0]
        maxEnd = intervals[0][1]
        for element in intervals:
            minStart = min(minStart, element[0])
            maxEnd = max(maxEnd, element[1])
        spectrum = [[0, 0] for _ in range(maxEnd - minStart + 2)] 
        #In the spectrum array, first member of the list member
        #is the number of intervals starting at a specific
        #point, the second member of the list member is the
        #number of intervals finishing at a specific point
        for element in intervals:
            spectrum[element[0] - minStart][0] += 1
            spectrum[element[1]- minStart][1] += 1
        answer = []
        acumStartPoints = 0
        acumEndPoints = 0
        currentStart = 0
        for index, element in enumerate(spectrum):
            if acumStartPoints == 0 and element[0]:
                currentStart = minStart + index
            acumStartPoints += element[0]
            acumEndPoints += element[1]
            if acumStartPoints and acumStartPoints == acumEndPoints:
                answer.append((currentStart, minStart + index))
                acumStartPoints = 0
                acumEndPoints = 0             
                
        return answer

if __name__ == '__main__':
    lst = [(5, 9), (15, 29), (10, 10), (6, 8), (20, 39), (11, 15), (2, 4)]
    print(Solution().mergeIntervals(lst))
