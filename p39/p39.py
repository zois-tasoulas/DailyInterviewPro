class Solution:
    def countWaterUnits(self, elevation):
        if not elevation:
            return 0
        length = len(elevation)
        total = 0
        maxElevation = elevation[0]
        maxOnLeft = [0 for _ in range(length)]
        leftMax = elevation[-1]
        for i in range(length - 2, 0, -1):
            maxOnLeft[i] = leftMax
            leftMax = max(leftMax, elevation[i])
        for i in range(length - 1):
            diff = min(maxElevation, maxOnLeft[i]) - elevation[i]
            if diff > 0:
                total += diff
            maxElevation = max(maxElevation, elevation[i])

        return total

if __name__ == '__main__':
    elevation = [0, 1, 0, 2, 1, 0, 1, 6, 2, 1, 2, 1]
    print(Solution().countWaterUnits(elevation))
