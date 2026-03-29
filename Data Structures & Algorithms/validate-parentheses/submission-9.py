class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')':'(', '}': '{', ']':'['}
        res = True
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if c in ')}]':
                    if len(stack) == 0 or pair[c] != stack.pop():
                        res = False
            
        if len(stack) > 0:
            return False 

        return res and len(stack) == 0