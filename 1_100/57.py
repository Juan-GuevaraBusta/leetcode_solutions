class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = nums[0]
        top_limit = nums[0]
        for i in range(1, len(nums)):
            top_limit = max(top_limit + nums[i], nums[i])
            ans = max(ans, top_limit)
        return ans
