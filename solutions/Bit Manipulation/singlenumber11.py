class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums))//2
    
#     solution2
#             in the second solution , you could solve it just the same way as solving the question on single number
        c= Counter(nums)
        for i in c:
            if c[i] == 1:
                return i
        
