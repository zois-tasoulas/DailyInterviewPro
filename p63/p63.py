class Solution:
    def calculateAngle(self, hours, minutes):
        """
        :type hour: int, mibutes: int
        :rtype: float
        """
        if hours > 11:
            hours -= 12
        if minutes == 60:
            minutes = 0
        # 360 / 60 * minutes
        minAngle = 6 * minutes
        # 360 / 12 * hours + 360 / 12 * minutes / 60
        hourAngle = 30 * hours + minutes / 2
        angle = abs(hourAngle - minAngle)
        return angle if angle < 180 else 360 - angle

if __name__ == '__main__':
    print(Solution().calculateAngle(21, 30))
