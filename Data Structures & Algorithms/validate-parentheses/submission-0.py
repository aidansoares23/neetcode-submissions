class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            elif char in pairs:
                # if the stack is empty, there's no 
                # valid opener bracket attached to this value
                if not stack:
                    return False
                if stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return not stack