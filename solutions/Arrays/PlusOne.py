class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1] #reverse the array
        carry = 1
        i = 0 #i is the index of positions of digits we're currently at
        while carry:
            if i < len(digits):
                if digits[i]==9:
                    digits[i]=0
                    carry = 1
                else:
                    digits[i]+=1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i+=1
        return digits[::-1]
