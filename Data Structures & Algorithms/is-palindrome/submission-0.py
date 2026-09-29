class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis=[]
        for i in s:
            if i.isalnum():
                lis.append(i)
        str_c = "".join(lis).lower()

        reversed = str_c[::-1]
        return True if str_c == reversed else False
        