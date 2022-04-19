# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string.
# For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

class Solution:
    def minDeletions(self, s: str) -> int:
        # collections is a datatype that works like dictionaries e.g s ="aaabbbcc" = [[a:3,b:3,c:2 in] collections]
        count = collections.Counter(s)
        used = set()
        result = 0
        
        for char , freq in count.items():
            while freq > 0 and freq in used:
                freq -=1
                result +=1
            used.add(freq)
        return result
        
