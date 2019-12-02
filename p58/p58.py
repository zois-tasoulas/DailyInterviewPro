class Solution:
    def reverseWords(self, string):
        """
        :type string: str
        :rtype: str
        """
        return " ".join(x[::-1] for x in string.split())

if __name__ == '__main__':
    sentence = "I'd need to study harder"
    print(Solution().reverseWords(sentence))
