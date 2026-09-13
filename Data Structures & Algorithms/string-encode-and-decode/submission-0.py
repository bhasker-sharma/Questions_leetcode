class Solution:

    def encode(self, strs: List[str]) -> str:
        result =[]
        for i in strs:
            store_this = str(len(i)) +'#'+ i
            result.append(store_this)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        res =[]
        i = 0
        while i < len(s):
            j=i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])
            words = s[j+1:j+1+length]
            res.append(words)
            i = j+1+length 
        return res
