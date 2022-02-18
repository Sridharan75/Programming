name=['Kamal','Ruwan','Nimal','Wimal']
datacount=len(name)
for i in range(datacount - 1):
    for k in range(i+1,datacount):
        if name[i]<name[k]:
            name[i],name[k]=name[k],name[i]
    print(name[i],name[k])
