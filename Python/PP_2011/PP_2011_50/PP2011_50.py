f1 =open('input.txt','r')
f2 =open('output.txt','w')
line=f1.readline()
while(line):
    data = (line.strip()).split(",")
    total = float(data[1])+float(data[2])
    f2.write('{},{},{},{}\n'.format(data[0],data[1],data[2],total))
    line=f1.readline()
f1.close()
f2.close()
