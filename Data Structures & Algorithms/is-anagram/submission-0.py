#input: string, output: bool where true if anagram false if not
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        elif (len(s) == 0 or len(t) == 0):
            return False
        
        s_sorted_list = sorted(s)
        t_sorted_list = sorted(t)
        s_sorted = ''.join(s_sorted_list)
        t_sorted = ''.join(t_sorted_list)

        if s_sorted == t_sorted:
            return True
        else:
            return False
