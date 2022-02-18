line =0
while line<=5:
    space=5
    while space>line:
        print(" ",end="")
        space = space-1
    star=0
    while star<=line:
        print("*",end=" ")
        star=star+1
    print("\n")
    line=line+1
