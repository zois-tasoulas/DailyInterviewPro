class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        cnt = 1
        mxm = 1
        prevLetter = s[0]
        for letter in s[1:]:
            if letter != prevLetter:
                cnt += 1
            else:
                cnt = 1
            prevLetter = letter
            if cnt > mxm:
                mxm = cnt
        return mxm

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx"))
    print(Solution().lengthOfLongestSubstring(""))
    print(Solution().lengthOfLongestSubstring("aabbccfgcc"))
    print(Solution().lengthOfLongestSubstring("r"))
