List=[3,2,4,1]
for j in range(1,len(List)):
    i=0
    key=List[j]
    i=j-1
    while i>=0 and key<List[i]:
        List[i+1]=List[i]
        i-=1
    List[i+1]=key
print(List)

        
