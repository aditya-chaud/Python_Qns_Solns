
#Ex1:
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5


# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5
# for this use print(j+1, end='') or for in in range(1,rows+1) and range(1,i+1) meaning start from 1 and end with rows.

# rows = 6
# # if you want user to enter a number, uncomment the below line
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for i in range(rows):
#     # nested loop
#     for j in range(i):
#         # display number
#         print(i, end=' ')
#     # new line after each row
#     print(' ')


#Ex2.
# 55555
# 4444
# 333
# 22
# 1 print(i,end="")

# 54321
# 4321
# 321
# 21
# 1 print(j,end="")

# rows=5
# for i in range(rows,-1,-1):
#     for j in range(i,0,-1):
#         print(i,end="")
#     print("")

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

# rows=5
# b=0
# for i in range(rows,0,-1):
#     b+=1
#     for j in range(0,i):
#         print(b,end=' ')
#     print("")

# Inverted pyramid with the same digit
# 5 5 5 5
# 5 5 5
# 5 5
# 5
# rows =4
# for i in range(rows,0,-1):
#     for j in range(0,i):
#         print(5,end=" ")
#     print("")


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# rows=5
# for i in range(rows+1, 0, -1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print("")


# 1
# 3 3
# 4 4 4
# 5 5 5 5
# rows=4
# for i in range()




# 1 
# 2 1
# 3 2 1
# 4 3 2 1

# rows =5
# for i in range(1,rows):
#     for j in range(i, 0,-1):
#         print(j, end=" ")
#     print("")


    
#    *
#   **
#  ***
# ****

# rows=4
# for i in range(1,rows+1):
#     for j in range(rows,0,-1):
#         if j>i:
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print(" ")

# def staircase(n):
#     pom = 1
#     for i in range(n):
#         print(" " * (n-pom)+("#"*pom))
#         pom+=1
# staircase(4)
