class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2 or len(s2) < len(s1):
            return False

        s1_mp = dict()
        mp = {}
        for i in range(0, len(s1)):
            s1_letter = s1[i]
            s1_mp[s1_letter] = s1_mp.get(s1_letter, 0) + 1
            s2_letter = s2[i]
            mp[s2_letter] = mp.get(s2_letter, 0) + 1
        
        l, r = 0, len(s1) - 1

        if mp == s1_mp:
            return True

        while r < len(s2) - 1:
            l += 1
            r += 1

            mp[s2[r]] = mp.get(s2[r], 0) + 1

            old_letter = s2[l-1]
            if old_letter in mp:
                mp[old_letter] -= 1
                if mp[old_letter] == 0:
                    del mp[old_letter]

            if mp == s1_mp:
                return True

        return False
        