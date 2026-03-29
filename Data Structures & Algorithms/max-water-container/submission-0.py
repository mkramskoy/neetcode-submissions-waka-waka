class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0
        for i, h1 in enumerate(heights):
            for j in range(i, len(heights)):
                maxVolume = max(maxVolume, min(h1,heights[j])*(j-i))
        
        # i=1,h1=7
        # j=2

        return maxVolume

