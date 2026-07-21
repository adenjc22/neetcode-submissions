class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = []

        PL = 0
        PR = len(heights) -1
        while PL < PR:
            if heights[PL] > heights[PR]:
                output.append(min(heights[PR], heights[PL])*(PR-PL))
                PR -= 1
            elif heights[PL] < heights[PR]:    
                output.append(min(heights[PR], heights[PL])*(PR-PL))
                PL +=1
            else:
                output.append(min(heights[PR], heights[PL])*(PR-PL))
                if heights[PL+1] >heights[PR-1]:
                    PR -=1
                PL +=1
                
        return max(output)

        
                

