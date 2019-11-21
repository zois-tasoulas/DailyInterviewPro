class Solution:
    def isOrdered(self, lst, letterOrder):
        length = []
        maxLength = 0
        for word in lst:
            length.append(len(word))
            maxLength = max(maxLength, len(word))
        d = {}
        index = 0
        for letter in letterOrder:
            d[letter] = index
            index += 1
        for i in range(1, len(lst)):
            isSortedFlag = False
            for j in range(min(length[i - 1], length[i])):
                if d[lst[i - 1][j]] > d[lst[i][j]]:
                    return False
                elif d[lst[i - 1][j]] < d[lst[i][j]]:
                    isSortedFlag = True
                    break
            #Check whether a shorter word follows a longer word
            if isSortedFlag == False:
                if length[i - 1] > length[i]:
                    if length[i] == 0 or d[lst[i - 1][length[i] - 1]] == d[lst[i][length[i] - 1]]:
                        return False

        return True

if __name__ == '__main__':
    words = ["z", "zyw", "zyw", "zywv", "m", "lkjihg", "azyx"]
    order = "zyxwvutsrqponmlkjihgfedcba"
    print(Solution().isOrdered(words, order))
    words2 = ["zxwvu", "zxwvut", "zxwv"]
    print(Solution().isOrdered(words2, order))
