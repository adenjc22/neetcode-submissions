class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        current = 0

        for i in nums:
            if nums[i] ==1:
                count +=1
            else:
                max = count
                count = 0

        return max