class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        setn = set(nums)
        while i in setn:
            i +=1
        return i

#         if len(nums) == 1:
#             if nums[0] == 1:
#                 return 2
#             return 1
#         sumValues = 0
#         sumIndex = 0
#         negative = 0
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] > len(nums):
#                 count +=1
#         if count == len(nums):
#             return 1
#         for i in range(len(nums)):
            
#             if nums[i] < 0 or nums[i] > len(nums):
#                 nums[i] = 0 
#             sumValues += nums[i]
#             sumIndex += i+1
#         return sumIndex - sumValues
            
        
            
            
            
            
