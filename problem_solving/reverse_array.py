def reverse_arr(a):
    reversed =[]
    start=len(a)-1
    for i in range(start, -1, -1):
        reversed.append(a[i])
    return reversed

if __name__ == "__main__":
    n=int(input("enter the number of items you want in your list: "))
    # listt=list(map(int, input("enter the items in the list: ").rstrip().split()))
    list1=[]
    for i in range(n):
        a=int((input("Enter the items in the list:")))
        list1.append(a)
    print("Original List",list1)
    rev=reverse_arr(list1)
    print("Reversed list",rev)



