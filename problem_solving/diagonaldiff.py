from math import sqrt
ar=[[1,2,3], [4,5,6], [7,8,9]]
a=0
b=0
n=len(ar)
for i in range(n):
    for j in range(len(ar[i])):
        if i==j:
            a+=ar[i][j]
        if (i+j==n-1):
            b+=ar[i][j]
diff=abs(b-a)
print(diff)

