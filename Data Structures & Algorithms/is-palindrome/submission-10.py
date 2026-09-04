class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '')
        clean = ''
        for c in s:
            if c.isalnum():
                clean += c
        print(clean)
        
        #two pointers
        i = 0
        j = len(clean)-1
        while True:

            if i >= j:
                break
            
            if clean[i] != clean[j]:
                return False

            i += 1
            j -= 1

        return True
