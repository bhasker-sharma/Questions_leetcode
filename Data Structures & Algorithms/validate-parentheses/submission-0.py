class Solution:
    def isValid(self, s: str) -> bool:
            dict_ = { ')': '(', '}': '{', ']': '[' }
            stack_ = []
            for i in s:
                if i in dict_:
                    if len(stack_) !=0 and stack_[-1] == dict_[i]:
                        stack_.pop()
                    else:
                        return False
                else:
                    stack_.append(i)
            
            if len(stack_) == 0:
                return True
            else:
                return False
        