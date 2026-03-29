class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i, num in enumerate(numbers):
            for j in range(i, len(numbers)):
                if num + numbers[j] == target:
                    result = [i+1,j+1]
                    break

            if len(result) > 0:
                break

        return result