#My soln. using regex and string slicing techniques. with tc and sc of O(n)
import re
s="A man, a plan, a canal: Panamaa"

result_string = re.sub(r'[^a-zA-Z]', '', s).lower()
if result_string==result_string[::-1]:
    print(f"The string {result_string} is palindrome.")
else:
    print(f"The string {result_string} is not palindrome.")