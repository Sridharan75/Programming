f1=open('input.txt','r')
f2=open('output.txt','w')
for line in f1:
    data = (line.strip()).split(",")
    total= float(data[1])+float(data[2])
    f2.write('%10s-%4d\n'%(data[0],total))
f1.close()
f2.close()
print(total)
