loop=True
total=0
counter=0
while(loop):
    marks=int(input("Enter your marks: "))
    if(marks==-1):
        loop=False
    else:
        total=total+marks
        counter=counter+1
average=total/counter
print("The Total of marks is ",total)
print("The Average is ",average)
