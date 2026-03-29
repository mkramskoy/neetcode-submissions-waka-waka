class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            print(r, l)
            m = l + int((r-l)/2) # 4

            if target == nums[m]: # 4 != 6 
                return m
            if target < nums[m]: # 4 < 6
                r = m - 1 # 3
            elif target > nums[m]:
                l = m + 1
        
        return -1