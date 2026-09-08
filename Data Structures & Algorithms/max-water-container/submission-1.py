class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        biggest_area = 0
        while left < right:
            width = right - left
            height_of_water = min(heights[left], heights[right])
            current_area = width * height_of_water
            biggest_area = max(current_area, biggest_area)
            if heights[left] > heights[right]:
                right -= 1
            else: 
                left += 1

        return biggest_area