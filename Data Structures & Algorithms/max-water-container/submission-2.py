class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        maxVol = 0
        while l < r:
            left = heights[l]
            right = heights[r]
            maxVol = max(maxVol, min(left,right)*(r-l))

            if left < right:
                l += 1
            else:
                r -= 1

        return maxVol
        

# height = [1,7,2,5,4,7,3,6]
# prefix = [1,7,7,7,7,7,7,7]
# suffix = [7,7,7,7,7,7,6,6]

            
