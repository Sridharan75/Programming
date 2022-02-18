List=[3,2,4,1]
for j in range (len(List)):
    i=0
    while i<len(List)-1:
        if(List[i]>List[i+1]):
            List[i+1],List[i]=List[i],List[i+1]
        i=i+1 
print(List)
        
