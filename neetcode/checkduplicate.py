#TC: O(n^2), becuase for two loops tc is O(n*n)
#SC: O(1) as  amount of additional space used does not grow with the size of the input array.
# arr=[2,3,4,2]
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         condition=False
#         if arr[i]==arr[j]:
#             print("true")
#             condition=True
#             break
#     if condition:
#         break
# if condition==False:
#     print("false")

#TC: O(nlog(n)), cause sorted function has tc of nlog(n) and for iterating tc is O(n). The dominant factor is sorting.
#SC: O(n), sorted function creates a sorted copy of the input array, requires additional space proportional to the size of the input array.
# arr=[2,3,5,4,2]
# sorted_arr=sorted(arr)
# count=1
# for i in range(len(sorted_arr)-1):
#     if sorted_arr[i]==sorted_arr[i+1]:
#         count+=1
# if count>1:
#     print("true")
# else:
#     print("flase")


#TC:n, the TC of checkduplicate is O(n) as it iterates through each array element once, with O(1) operations inside the loop.
#SC:O(n), because the function creates a set to store unique elements, growing linearly with the input array size.
def checkduplicate(arr):
    sett=set()
    for n in arr:
        if n in sett:
            return True
        sett.add(n)
    return False
        
arr=[3,2,4,5,6,2]
result=checkduplicate(arr)
print(result)


    

























