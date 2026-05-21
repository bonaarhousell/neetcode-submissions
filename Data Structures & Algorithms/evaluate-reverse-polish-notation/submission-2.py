class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == "+":
                s.append(s.pop() + s.pop())
            elif t == "-":
                x,y = s.pop(),s.pop()
                s.append(y - x)
            elif t == "*":
                s.append(s.pop() * s.pop())
            elif t == "/":
                x,y = s.pop(), s.pop()
                s.append(int(y / x))
            else:
                s.append(int(t))
        return s[0]