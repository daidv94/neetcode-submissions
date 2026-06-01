class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            
            if c in closeToOpen:
                if not stack or closeToOpen[c] != stack[-1]:
                    return False
                stack.pop()
            
        return len(stack) == 0