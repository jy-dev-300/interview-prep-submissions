class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dict -> 공통 특징값 : group 
        d = {}
        for str in strs:
            key = tuple(sorted(str))
            if key in d:
                d[key].append(str)
            else:
                d[key] = [str]
        ans = []
        for key in d:
            ans.append(d[key])
        return ans
            

                

