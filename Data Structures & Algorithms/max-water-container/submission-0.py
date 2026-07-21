class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = []

        PL = 0
        PR = len(heights) -1
        while PL <PR:
            if heights[PL] > heights[PR]:
                output.append(heights[PR]*(PR-PL))
                PR -= 1
            output.append((heights[PL])*(PR-PL))
            PL +=1
        return max(output)

        
                

