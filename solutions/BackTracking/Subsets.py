class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #solve it iteratively
        #use cascading method, 
        #output = [[]]
        #step1: add each number in nums inside the array which is inside the output array
        #[[],[1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
        output = [[]]
        for i in nums:
            output += [o + [i] for o in output]
        return output
            
