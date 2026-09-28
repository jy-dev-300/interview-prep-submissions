class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for c in s:
            if c not in d1.keys():
                d1[c] = 0
            else:
                d1[c] += 1
        for c in t:
            if c not in d2.keys():
                d2[c] = 0
            else:
                d2[c] += 1
        if d1 == d2:
            return True
        else:
            return False