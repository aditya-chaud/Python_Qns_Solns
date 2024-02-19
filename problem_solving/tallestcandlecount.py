#count the largest element in an array
arr=[3,2,4,3,5,4,5,3,5]
tall=arr[0]
count=0
for i in range(len(arr)):
    if arr[i]>tall:
        tall=arr[i]
        count=1
    elif (arr[i]==tall):
        count+=1
print(count)
