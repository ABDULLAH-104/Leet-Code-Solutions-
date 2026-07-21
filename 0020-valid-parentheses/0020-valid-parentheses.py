class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in pairs:
                # It's a closing bracket
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                # It's an opening bracket
                stack.append(char)
        
        return not stack  # valid only if everything was matched