class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, v1 in enumerate(nums):
            for i2, v2 in enumerate(nums):
                if i1 == i2:
                    continue
                
                if v1+v2 == target:
                    return [i1, i2]
        