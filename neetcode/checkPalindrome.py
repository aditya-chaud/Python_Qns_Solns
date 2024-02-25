#My soln. using regex and string slicing techniques. with tc and sc of O(n)
# import re
# s="2A man, a plan, a canal: Panama2"

# result_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
# if result_string==result_string[::-1]:
#     print(f"The string {result_string} is palindrome.")
# else:
#     print(f"The string {result_string} is not palindrome.")

# Modified version with TC of O(n) but SC of O(1)
class Solution:
    def isPalindrome(self, s):
        l=0
        r=len(s)-1
        # Loop until the pointers meet in the middle
        while l<r:
            # Move the left pointer (l) to the right until it finds an alphanumeric character
            while l<r and not self.alphaNum(s[l]):
                l+=1
            # Move the right pointer (r) to the right until it finds an alphanumeric character
            while r>l and not self.alphaNum(s[r]):
                r-=1
            # Check if the characters at l and r are different (ignoring case)
            if s[l].lower() != s[r].lower():
                return False
            # Move pointers closer to the center for the next comparison
            l=l+1
            r=r-1
        # If the loop completes without finding any mismatches, the string is a palindrome and returns True
        return True
    
    # function to check if a character is alphanumeric
    def alphaNum(self,c):
        return (ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"))
# Create an instance of the Solution class
sol=Solution()

# Test the isPalindrome function with a sample string
str="race car@"
result=sol.isPalindrome(str)
print(result)
