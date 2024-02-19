# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
arr=[2,3,5,6,7]
arr=sorted(arr)
minsum=0
maxsum=0
for i in range(len(arr)-1):
    minsum+=arr[i]
for i in range(len(arr)-1,0,-1):
    maxsum+=arr[i]
print(str(minsum) + "  " + str(maxsum))