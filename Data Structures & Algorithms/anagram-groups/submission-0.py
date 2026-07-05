class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d ={}
        for i in strs:
            key = tuple(sorted(i))
            x = d.get(key, [])
            x.append(i)
            d[key] = x
        return list(d.values())