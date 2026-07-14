class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        current = 0

        for i in range(nums+1):
            if i ==1:
                current +=1
            else:
                max = current
                current = 0

        return max