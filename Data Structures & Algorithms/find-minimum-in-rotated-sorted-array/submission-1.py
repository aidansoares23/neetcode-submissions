class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0] # grab first value to init result
        # init left and right pointers at start and end of array
        left, right = 0, len(nums) - 1 

        # Iterate across array while the pointers haven't met yet
        while left <= right:
            # If we find ourselves in a subarray that is sorted
            if nums[left] < nums[right]:
                # Then the furtherst left value is the smallest
                # Compare that value from our previous smallest result
                result = min(result, nums[left]) 
                break
            # Otherwise, we are in some array that needs a midpoint
            mid = (left + right) // 2
            # Compare previous result/minimum against current midpoint
            result = min(result, nums[mid])
            if nums[mid] >= nums[left]: # we are in left sorted portion
                left = mid + 1
            else: # we are in right sorted portion
                right = mid - 1
        return result