class Solution:
    def longestSubstringWithKCharacters(self, string, k):
        if len(string) < k:
            return len(string)
        longest = 0
        length = 0
        d = {}
        for i in range(0, len(string)):
            if string[i] in d:
                length += 1
                d[string[i]] = i
            elif len(d) < k:
                d[string[i]] = i
                length += 1
            else:
                mnm = i
                for j in d.keys():
                    if d[j] < mnm:
                        mnm = d[j]
                        letter = j
                del d[letter]
                d[string[i]] = i
                length = i - mnm
            longest = max(longest, length)

        return longest

if __name__ == '__main__':
    string = "aabcdefffasdutk49gmvheuwn39j59gk"
    k = 5
    print(Solution().longestSubstringWithKCharacters(string, k))
