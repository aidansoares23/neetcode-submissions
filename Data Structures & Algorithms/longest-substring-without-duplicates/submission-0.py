class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]

            while char in seen:
                seen.remove(s[left])
                left += 1 

            seen.add(char)

            current_length = len(seen)
            longest = max(longest, current_length)
        return longest