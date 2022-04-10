    def singleNumber(self, nums: List[int]) -> int:
        #solution 1
        c = Counter(nums)
        for i in nums:
            if c[i] == 1:
                return i
        
        
        #solution2
        a = 0 
        for i in nums:
            a^= i
            return a
