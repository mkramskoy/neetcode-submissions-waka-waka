class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True

        str = "".join(char.lower() for char in s if char.isalnum())

        # shorter version
        # newStr == newStr[::-1]
        for i in range(int(len(str)/2)):
            if str[i] != str[len(str)-i-1]:
                print(str[i])
                print(str[len(str)-i-1])
                result = False
                break
            
        return result