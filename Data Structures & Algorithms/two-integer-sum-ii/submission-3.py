class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Sorted & O(1) additional space screams two pointer
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            elif current_sum > target: 
                right -= 1
        # There will always be exactly one valid solution, no base case needed