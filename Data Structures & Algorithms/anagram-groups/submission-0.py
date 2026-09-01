class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for str in strs:
            key = tuple(sorted(str))
            if key in d:
                d[key].append(str)
            else:
                d[key] = [str]
        
        soln = []
        for key in d:
            soln.append(d[key])
        return soln
                

