class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = count = 0
        for i in nums:
            if i == 0:
                best = max(best, count)
                count = 0
            else:
                count += 1

        return max(count, best)