class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        dict = {}
        for i, num in enumerate(nums):
            counter = 0
            while counter < len(nums):
                if counter is i:
                    counter += 1
                    continue
                else:
                    if counter not in dict:
                        dict[counter] = num
                    else:
                        dict[counter] = dict[counter] * num
                    
                    counter += 1

    
        # sort by key as int
        result = [dict[key] for key in sorted(dict.keys(), key=int)]    
    
        return result
