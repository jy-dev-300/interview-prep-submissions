class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < (len(s)):
            j = i

            # find the #
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            # string starts right after #
            start = j + 1
            end = start + length

            res.append(s[start:end])

            #jump to next encoded string
            i = end

        return res
