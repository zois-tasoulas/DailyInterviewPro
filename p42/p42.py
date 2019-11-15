class Solution:
    def lookAndSay(self, n):
        if n == 0:
            return None
        prevSequence = [1]
        currentSequence = []
        for _ in range(n - 1):
            currentSequence.append(1)
            for i in range(1, len(prevSequence)):
                if prevSequence[i] == prevSequence[i - 1]:
                    currentSequence[-1] += 1
                else:
                    currentSequence.append(prevSequence[i - 1])
                    currentSequence.append(1)
            currentSequence.append(prevSequence[-1])
            prevSequence = currentSequence
            currentSequence = []

        return "".join(str(element) for element in prevSequence)

if __name__ == '__main__':
    for i in range(15):
        if i == 1:
            print("%dst term is:" % i, end=' ')
        elif i == 2:
            print("%dnd term is:" % i, end=' ')
        elif i == 3:
            print("%drd term is:" % i, end=' ')
        else:
            print("%dth term is:" % i, end=' ')
        n = i
        print(Solution().lookAndSay(n))
