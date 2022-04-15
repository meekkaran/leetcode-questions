class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle = hare = nums[0] #initialise two pointers at the beginning of the list
        turtle = nums[turtle] #moves one position
        hare = nums[nums[hare]] #moves two positions
        
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[nums[hare]]
        turtle = nums[0]
        
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[hare]
        return turtle
    
    
    #solution2 
    #you could use dictionary because it does not pick duplicates
    dict1 = {}
    for i in nums:
        if i in dict1:
            return i
        dict1[i] = 1
