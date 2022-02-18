data = [5,1,23,10]
datacount=len(data)
for i in range(datacount-1):
    for k in range(i,datacount):
        if data[i]>data[k]:
            temp=data[i]
            data[i],data[k]=data[k],temp
for i in range(datacount):
    print(data[i])
