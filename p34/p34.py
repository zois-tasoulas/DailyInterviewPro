class Solution:
    def stockProfit(self, prices):
        maxProf = 0
        if prices:
            minPrice = prices[0]
        for element in prices:
            maxProf = max(maxProf, element - minPrice)
            minPrice = min(minPrice, element)
        return maxProf

if __name__ == '__main__':
    lst = [5, 2, 4, 7, 15, 1, 6, 3, 2, 10]
    print(Solution().stockProfit(lst))
