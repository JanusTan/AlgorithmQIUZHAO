# 55. 跳跃游戏
# 时间复杂度O(n), 空间复杂度O(1)，用的是贪心思想，每次走都是不回头，而且走的都是最优的步数


def canJump(nums):
    max_i = 0
    for i, jump in enumerate(nums):
        if i <= max_i < i + jump: # 当还在最优步数范围，但是出现了更加最优的步数
            max_i = i + jump
    return max_i >= i
