#1. initialize a new 2d array with [1,2,3] in the first row and [5,6,7] 
# in the second row. Store it in new vaiable called a_2d
a_2d=[[1,2,3],[5,6,7]]
print(a_2d)
#2. replace the number 6 with number 99
a_2d[1][1]=99
print(a_2d)
#3. Iterate over a_2d and print using for i in range() syntax
for i in range(len(a_2d)):
    for j in range(len(a_2d[i])):
        print(a_2d[i][j])
        
#3. For the given 2d array with equal no of rows and colns. write a function that adds up the 
#diagonal elements and returns the sum.

def diagonal_sum(b):
    sum=0
    for i in range(len(b)):
        sum+=b[i][i]
    return sum

b_2d=[[2,3,4],[3,5,7],[6,1,2]]
print(diagonal_sum(b_2d))