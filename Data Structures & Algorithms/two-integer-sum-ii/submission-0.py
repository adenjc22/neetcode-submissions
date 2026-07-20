class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        PL = 0
        PR = len(numbers) -1

        #for i,x in enumerate(numbers):
        #    d[x] = i

        #print(d)
        while PL < PR:
            sumx = numbers[PL] + numbers[PR]
            if sumx >target:
                PR -= 1
            elif sumx < target:
                PL += 1
            elif sumx ==target:
                return [numbers[PL],numbers[PR]]

            
                
