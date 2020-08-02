# 50. Pow(x, n)
# 时间复杂度：O(logn)，即为递归的层数。
# 空间复杂度：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(n):
            # terminator
            if n==0:
                return 1.0
            # prepare data, conquer subproblems
            y = quickMul(n//2) # 双斜杠是除法向下取整-3//2=-2
            # process and generate the final result
            # if n % 2 == 0:
            #     return y*y
            # else:
            #     return y*y*x
            return y * y if n % 2 == 0 else y * y * x
            # revert the current level state
        if n < 0:
            return 1/quickMul(-n)
        else:
            return quickMul(n)