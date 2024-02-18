#calculate the ratio of proportion of +ve, -ve and 0s in the list.


arr=[1,2,3,-1,-5,0,0]
po=0
ne=0
ze=0
for i in arr:
    if i>0:
        po+=1
    elif i<0:
        ne+=1
    else:
        ze+=1
po_ratio=round(po/len(arr),6)
ne_ratio=round(ne/len(arr),6)
ze_ratio=round(ze/len(arr),6)
print(po_ratio,ne_ratio,ze_ratio)