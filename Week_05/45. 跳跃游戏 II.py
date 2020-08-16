class Solution:
    def jump(self, nums: List[int]) -> int:
        # 贪心思想，每次都找能到达最远的下标中最大的进行跳跃
        max_step = 0
        end = 0 # 记录当前能走的最远下标
        step = 0
        for i in range(len(nums)-1): # 不需要遍历到最后一个
            max_step = max(max_step, nums[i] + i) # 寻找当前下标能到达的最远下标
            if (i == end): # 当遍历到的下标和当前能走最远时，更新最远下标
                end = max_step
                step += 1
        return step