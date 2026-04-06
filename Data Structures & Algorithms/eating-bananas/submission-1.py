class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r

        while l <= r:
            m = (l + r) // 2

            hours_left = h
            for pile in piles:
                hours_left -= math.ceil(pile / m)

            if hours_left < 0:
                l = m + 1
            elif hours_left >= 0:
                res = m
                r = m - 1

        return res

            
