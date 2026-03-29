class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num not in hashMap.keys():
                hashMap[num] = True
            else:
                return True
        
        return False