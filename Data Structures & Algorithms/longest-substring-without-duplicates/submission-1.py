class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        wordStart = 0
        res = 0

        for r in range(len(s)):
            if s[r] in map:
                wordStart = max(map[s[r]] + 1, wordStart)
            map[s[r]] = r
            res = max(res, r - wordStart + 1)
        return res