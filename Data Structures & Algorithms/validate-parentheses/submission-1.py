class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(",
                "]": "[",
                "}": "{"
        }

        stack = []
        
        for n in s:
            if n in map:
                if stack and stack[-1] == map[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)

        if not stack: return True
        return False