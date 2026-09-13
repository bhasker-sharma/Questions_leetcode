class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            num_set = set(nums)
            longest = 0
            for i in num_set:
                if (i-1) in num_set:
                    continue
                start = i
                counter = 1
                while start+1 in num_set:
                        start += 1
                        counter += 1
                longest = max(longest,counter)
            return longest  