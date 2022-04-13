class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
         nums.sort()  # sort the numbers before converting the list to a tuple
        ans = [[]]
        for n in nums:
            temp=[]
            for l in ans:
                temp.append(l+[n])
            ans.extend(temp)
           
        #1.convert the list into  a tuple       [tuple(l) for l in ans]
        #2.make it a set                        set([tuple(l) for l in ans])
        #3.then reconvert it into a list        list[l] for l in set([tuple(l) for l in ans])
        return [list(l) for l in set([tuple (l) for l in ans])]
