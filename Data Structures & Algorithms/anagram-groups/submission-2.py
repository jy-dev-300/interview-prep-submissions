class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} #k: anagram v: list of words
        res = []
        for s in strs:
            anagram = ''.join(sorted(s))
            if anagram in d:
                d[anagram].append(s)
            else:
                d[anagram] = [s]
        for anagram in d:
            res.append(d[anagram])
        return res
        
        




        

                

