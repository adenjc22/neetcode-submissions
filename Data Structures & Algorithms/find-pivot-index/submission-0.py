class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left = 0
        for i in nums:
            right = sum(nums) - left - i
            if left == right:
                return i
            left += i
        return -1