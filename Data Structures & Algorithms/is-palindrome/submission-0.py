class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        #Initialize pointers at beggining and end

        while l < r:
        # iterate until pointers meet each other
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # skip if the pointer is at a non alphanum
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # skip if the pointer is at a non alphanum
            if s[l].lower() != s[r].lower():
                return False
            #if pointers dont have the same alphanum char, return false
            l, r = l + 1, r - 1    
            # move pointers

        return True

    #Function to check if is alphanum
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))


#