class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j =0,0
        z = []
        for x in range(len(t)):
            if s[i] == t[j]:
                z.append(s[i])
                i += 1
                j += 1
            else: 
                j+= 1

        if i == len(s):
            return True
        return False

        
        

        
                