class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        i = 0
        while cnt < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
            cnt += 1
