class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior = []
        
        for i in details:
            if i != int(details[i]):
                senior.append(i)

        return senior