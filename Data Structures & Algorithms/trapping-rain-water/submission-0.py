class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        suffix = [0]

        for i in range(1, len(height)): 
            prefix.append(max(prefix[i-1], height[i-1]))

            j = len(height) - 1 - i
            suffix.insert(0, max(suffix[0], height[j+1]))

        print(prefix)
        print(suffix)

        result = 0
        for i in range(len(height)):
            water = max(0, min(prefix[i],suffix[i]) - height[i])
            print(water)
            result += water

        return result
