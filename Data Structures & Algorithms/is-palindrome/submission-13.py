class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '')
        clean = ''
        for c in s:
            if c.isalnum():
                clean += c
        print(clean)
        
        d1 = []
        d2 = []
        for i, char in enumerate(clean):
            d1.append(char)
        for j in range(len(clean)-1, -1, -1):
            d2.append(clean[j])
        print(d1)
        print(d2)
        if d1==d2:
            return True
        else:
            return False

