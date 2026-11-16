class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        cmax = nums[0]
        cmin = nums[0]
        for i in range(1, len(nums)):
            tmp_max = cmax * nums[i]
            tmp_min = cmin * nums[i]
            cmax = max(nums[i], tmp_max, tmp_min)
            cmin = min(tmp_min, tmp_max, nums[i])
            ans = max(ans, cmax)
        return ans
        
