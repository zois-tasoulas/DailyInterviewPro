from collections import defaultdict

class Solution:
    def groupAnagrams(self, lst):
        """
        :type lst: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(lambda: [])
        for word in lst:
            d[tuple("".join(sorted(word)))].append(word)
        return list(d.values())

if __name__ == '__main__':
    lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(lst))
