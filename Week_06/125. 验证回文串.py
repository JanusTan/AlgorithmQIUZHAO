import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 提取出字母数字
        # 双指针验证回文
        if not s: return True
        letters_nums = []
        nums = "0123456789"
        for i in s:
            if i in (nums + string.ascii_letters):
                letters_nums.append(i.lower())
        print(letters_nums)
        left, right = 0, len(letters_nums)-1
        while left<right:
            if letters_nums[left] == letters_nums[right]:
                left += 1
                right -= 1
            else: return False
        return True