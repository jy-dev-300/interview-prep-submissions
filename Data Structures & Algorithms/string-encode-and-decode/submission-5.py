class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            out += str(len(s)) + '_' + s
        return out

    def decode(self, s: str) -> List[str]:
        # keep collecting char until we encounter the next _
        # count = collected count_str
        # 
        out = []
        i=0
        while i < len(s):
            count_str = ''
            while s[i] != '_':
                count_str += s[i]
                i+=1
            i += 1
            out.append(s[i:i+int(count_str)])
            i += int(count_str)
        return out

