class Solution:
    def maxArea(self, heights: List[int]) -> int:
        prefix = []
        suffix = []

        hLeft = 0 
        hRight = 0 
        for i in range(len(heights)):   
            hLeft = max(hLeft, heights[i])
            prefix.append(hLeft)

            j = len(heights) - 1 - i
            hRight = max(hRight, heights[j])
            suffix.insert(0, hRight)

        print(prefix)
        print(suffix)

        l,r = 0, len(heights) - 1
        maxVol = 0
        while l != r:
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

            
