class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def subsets(i: int):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            subsets(i+1)

            subset.pop()
            subsets(i+1)

        subsets(0)

        return res