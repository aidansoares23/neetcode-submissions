class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                if seen[complement] < i:
                    return [seen[complement] + 1, i + 1]
                else:
                    return [i + 1, seen[complement] + 1]
            seen[num] = i
        return []