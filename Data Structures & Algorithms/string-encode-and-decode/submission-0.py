class Solution:
    def encode(self, strs: List[str]) -> str:
        lengths = []
        result = ""
        for str in strs:
            result += f'{len(str)},'
            result += f'{str}'

        return result
        
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        result = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != ",":
                length += s[i]
                i += 1
            i += 1
            
            length = int(length)
            word = s[i:i+length]
            i += length

            result.append(word)

        return result