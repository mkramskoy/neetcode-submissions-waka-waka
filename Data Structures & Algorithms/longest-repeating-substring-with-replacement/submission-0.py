class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l, r = 0, 0
        res = 0

        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1

            # check if map fullfill the requirement
            # r-s+1 - max(mp.values()) < k
            # if not move the windown until it fullfills
            while r - l + 1 - max(mp.values()) > k:
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l += 1

            res = max(res, sum(mp.values()))

        return res
