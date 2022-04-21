class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        #two pointers, left and right pointers
        l=0
        r = len(nums)-1
        while l <= r:
            #if the square of the value at the left pointer is less that the square of the value at the right pointer, append the value at the              right pointer to the result then shift the right pointer backwards and vice versa
            if nums[l]*nums[l] < nums[r]*nums[r]:
                res.append(nums[r]*nums[r])
                r -= 1
            else:
                res.append(nums[l]*nums[l])
                l += 1
        return res[::-1]#reverse the result since you've been appending the values to the result
