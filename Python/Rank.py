Nos=int(input("Number of students: "))
Sum=[]
Rank={}
#f=open("Rank.txt","a")

while Nos>0:
    
    Name=input("Name: ")
    
    #Getting marks for 3 subjects
    count=1
    total=0
    while count<=3:
        marks=int(input("Enter your marks: "))
        total=total+marks
        count=count+1
    Sum.append(total)
    Nos=Nos-1
    
    #Save Totals with names
    Rank[total]=Name
     
#For- Sorting by rank
for j in range(len(Sum)):
    i = 0
    while i<len(Sum)-1:
        if Sum[i]<Sum[i+1]:
            Sum[i],Sum[i+1] = Sum[i+1],Sum[i]
        i = i+1

#write in Rank.txt
num=1
for k in Sum:
    print("{}-{}-{}".format(Rank[k],k,num))
    #f.write(str(Rank[k]))
    #f.write(" - ")
    #f.write(str(k))
    #f.write(" - ")
    #f.write(str(num))
    #f.write("\n")
    num=num+1
#print("Done!!!")
#f.close()
