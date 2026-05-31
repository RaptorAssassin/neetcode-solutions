class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif t == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif t == "-":
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                stack.append(o2 - o1)
            elif t == "/":
                o1 = int(stack.pop())
                o2 = int(stack.pop())
                stack.append(int(o2 / o1))
            else:
                stack.append(int(t))

        return stack.pop()