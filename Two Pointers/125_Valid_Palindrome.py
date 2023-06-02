class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pnt = ""
        right_pnt = ""
        for i in range(0, len(s)):
            if s[i].isalnum():
                left_pnt += s[i].lower()
            if s[len(s) - 1 - i].isalnum():
                right_pnt += s[len(s) - 1 - i].lower()
        if left_pnt == right_pnt:
            return True
        return False


# More Efficient 2 pointers
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
