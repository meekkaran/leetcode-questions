class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""# create a res string to hold the result
        for char in s:# loop through s
            if char.isalnum():# check if current element is alphanumeric
                result+=char.lower()# add the current element in its lower case version
                print(result)
        return result == result [::-1]# check if res is equal when reversed 
