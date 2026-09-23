class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]: 
        lis = [0]*len(temperatures)
        stack =[]
        for idx,val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                popped = stack.pop()
                distance = idx - popped
                lis[popped] = distance
            stack.append(idx)
        return lis