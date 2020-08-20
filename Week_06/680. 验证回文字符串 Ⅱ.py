class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 双指针检测，当字符相等则左+右-，否则左去掉一个或者右去掉一个
        def check_palindrome(left, right):
            while left<right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else: return False
            return True
        low, high = 0, len(s)-1
        while low<high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return check_palindrome(low+1, high) or check_palindrome(low, high-1)
        return True
