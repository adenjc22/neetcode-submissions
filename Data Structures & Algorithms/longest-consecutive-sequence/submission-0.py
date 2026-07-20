class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        X = 0

        for i in s:
            if (i -1) not in s:
                L =1
                while (i + L) in s:
                    L+=1
                X = max(L,X)
        return X

            
                


        
            