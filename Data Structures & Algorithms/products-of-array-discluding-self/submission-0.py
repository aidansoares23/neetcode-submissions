class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [0] * size
        prefix = [0] * size
        suffix = [0] * size

        prefix[0] = suffix[size - 1] = 1
        for i in range(1, size): 
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(size - 2, -1, -1): 
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(size): 
            result[i] = prefix[i] * suffix[i]
        return result