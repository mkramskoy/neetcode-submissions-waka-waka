class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l<=r:
            m = (l + r) // 2
            m_num = nums[m]

            if m_num == target:
                return m

            # left half is sorted
            if nums[l] <= m_num:
                if nums[l] <= target < m_num:
                    r = m - 1
                else:
                    l = m + 1
            # right half is sorted
            else:
                if m_num < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1