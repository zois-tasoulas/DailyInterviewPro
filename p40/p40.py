class Solution:
    def buddyStrings(self, string1, string2):
        length = len(string1)
        if length != len(string2):
            return False
        if string1 == string2:
            return length > len(set(string1))
        differences = 0
        for i in range(length):
            if string1[i] != string2[i]:
                differences += 1
                if differences == 1:
                    char1 = string1[i]
                    char2 = string2[i]
                else:
                    if char1 != string2[i] or char2 != string1[i]:
                        return False
            if differences > 2:
                return False
        return True

if __name__ == '__main__':
    string1 = "aaafrvcs"
    string2 = "asafrvca"
    print(Solution().buddyStrings(string1, string2))
