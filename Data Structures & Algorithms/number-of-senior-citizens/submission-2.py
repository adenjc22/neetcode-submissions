class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior = []
        
        for i in details:
            age = i[11:13]
            if age >= 65:
                senior.append(i)

        return senior