# TC: O(n^2) 
#  This is due to the two nested loops, each iterating over the entire array.
# SC: O(1) - because the extra space used does not depend on the size of the input array.
# for the input array: nums[2,3,1] and target=5, the output should be index of 2,3 ie [0,1] because 2+3=5
#Brute force
# nums=[3,1,1]
# target=2
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print([i,j])


#Hashmap
#TC:O(n) SC:O(n)
def twoSum(nums, target):
    hashMap={} # numbers:index
    for i in range(len(nums)):
        hashMap[nums[i]]=i
            
        for i in range(len(nums)):
            y=target-nums[i]
            #checking y as key, if it is present in hashMap
            if y in hashMap and hashMap[y]!=i:
                return [hashMap[y],i]


nums=[3,4,2]
target=6
result=twoSum(nums,target)
print(result)


# hashmap={3:0, 4:1,2:2}
# i=0
# y=6-nums[0]=6-3=3
# 3 in hashMap{} looks for key, yes and hashMap[3]=0 !=0 False so loop continues
    
# i=1
# y=6-4=2
# 2 in hashMap{} looks for key, yes and hashMap[2]=2 !=1 True so loop stops. 
# hence
# return [hashMap[2], 1]=[2,1]
