class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1, dict2 = {}, {}
        if len(s) != len(t):
            return False

        for a, b in zip(s, t):
            dict1[a] = dict1.get(a, 0) + 1
            dict2[b] = dict2.get(b, 0) + 1

        return dict1 == dict2
