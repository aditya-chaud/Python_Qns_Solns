#Compare a[0] with b[0], a[1] with b[1] and b[0] with b[1] and then 
# If a[i] > b[i], then Alice(a) is awarded 1 point.
# If a[i] < b[i], then Bob(b) is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.

a=[3,4,2]
b=[4,5,1]
ilist=list(zip(a,b))
print("iterable pairs: ",ilist)
count_a=0
count_b=0
for i, j in ilist:
    if i>j:
        count_a+=1
    if i<j:
        count_b+=1
    else:
        pass
print("Total points for a and b respectively are: ",count_a, count_b)




