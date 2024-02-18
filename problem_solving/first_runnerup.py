def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if (arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr


if __name__ == '__main__':
    n = int(input("Enter the number of items you want in your list:"))
    arr=[]
    for i in range(n):
        a=int(input("enter the numbers:"))
        arr.append(a)
    sorted_ar=bubble_sort(arr)
    print(sorted_ar[len(sorted_ar)-2])

# #Prints the second largest element from the list.
# if __name__ == '__main__':
#     n=int(input())
#     arr = list(map(int, input().split()))
#     max = arr[0]
#     second = -100
#     for x in arr:
#         if max < x:
#             max = x
#     for i in arr:
#         if second < i and i != max:
#             second = i
#     print(second)


