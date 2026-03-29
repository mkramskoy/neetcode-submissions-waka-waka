class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestChain = 0
        for num in nums:
            if num-1 in numSet:
                continue

            i = 0
            chainLen = 0
            while num+i in numSet is not None:
                chainLen += 1
                i += 1
            
            if chainLen > longestChain:
                longestChain = chainLen
            
        return longestChain