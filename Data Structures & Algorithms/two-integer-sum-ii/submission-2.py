class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(N)
        # seen = {}
        # for i, num in enumerate(numbers):
        #     complement = target - num
        #     if complement in seen:
        #         if seen[complement] < i:
        #             return [seen[complement] + 1, i + 1]
        #         else:
        #             return [i + 1, seen[complement] + 1]
        #     seen[num] = i
        # return []

        # Sorted & O(1) additional space screams two pointer
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return []