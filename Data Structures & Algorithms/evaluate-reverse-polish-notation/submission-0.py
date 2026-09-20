class Solution:
    def evalRPN(self, tokens: list[str]) -> int:  # this si the question of reverse polish notation
        ans = []
        for i in tokens:
            if i == '*':
                a= ans.pop()
                b= ans.pop()
                res = b*a
                ans.append(res)
            elif i == '+':
                a= ans.pop()
                b= ans.pop()
                res = b+a
                ans.append(res)
            elif i == '-':
                a= ans.pop()
                b= ans.pop()
                res = b-a
                ans.append(res)
            elif i == '/':
                a= ans.pop()
                b= ans.pop()
                res = b/a
                ans.append(int(res))
            else:
                ans.append(int(i))
        return ans[-1]