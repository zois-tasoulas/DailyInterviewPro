class Solution:
    def isPalindrome(self, s):
        if len(s) < 2:
            return True
        elif s[0] == s[-1]:
            return self.isPalindrome(s[1:-1])
        else:
            return False

    def longestPalindrome(self, s):
        if self.isPalindrome(s):
            return s
        a = self.longestPalindrome(s[1:])
        b = self.longestPalindrome(s[:-1])
        if len(a) > len(b):
            return a
        else:
            return b

if __name__ == '__main__':
    s = "tracecars"
    print(str(Solution().longestPalindrome(s)))
    s = "banana"
    print(str(Solution().longestPalindrome(s)))
    s = "advfaradalrgmadamjabamad"
    print(str(Solution().longestPalindrome(s)))
