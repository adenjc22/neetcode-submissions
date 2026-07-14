class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            if int(details[11:13]) > 60:
                count += 1

        return count
    

