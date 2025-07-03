class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        stack = []
        for char in s:
            if char in pair:
                stack.append(char)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if pair[prev] != char:
                    return False
                
        return len(stack) == 0