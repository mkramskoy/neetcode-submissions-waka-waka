class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True

        str = "".join(char for char in s if char.isalnum())
        print(str)

        for i in range(int(len(str)/2)):
            if str[i].lower() != str[len(str)-i-1].lower():
                print(str[i])
                print(str[len(str)-i-1])
                result = False
                break
            
        return result