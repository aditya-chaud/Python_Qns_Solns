#Runtime:41ms, memory:12.91MB
#My soln with TC of O(nlogn)
# s="anagram"
# t="granama"
# sSort= ''.join(sorted(s))
# tSort=''.join(sorted(t))
# if sSort==tSort:
#     print("true")
# else:
#     print("false")
 



#Using hash map. which can be initialized using dictionary in python
#TC:O(n) and SC:O(n)
def checkAnagram(s,t):
    # initialize two empty dict to count the values if each characters as key:value pairs
    countS={}
    countT={}
    if len(s)!=len(t):
        return False
    
    #counting the occurances of characters
    for char in s:
        countS[char] = countS.get(char,0) + 1
    for char in t:
        countT[char] = countT.get(char,0) + 1
    
    #comparing the counts of charactrs in hashmap
    for key in countS:
        #comparing the numbers of each characters in both dict 
        if countS[key] != countT.get(key,0):
            return False
    
    return True

s="anagram"
t="gramaan"
result=checkAnagram(s,t)
print(result)
