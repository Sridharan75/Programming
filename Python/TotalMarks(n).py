noOfStudents=int(input("How many Student mark you want to add: "))
total=0
counter=0
average=0
while(noOfStudents>0):
    marks=int(input("Enter Student marks here: "))
    total=total+marks
    noOfStudents=noOfStudents-1
    counter=counter+1
average=total/counter
print("The Total of marks is ",total)
print("The Average is ",average)
