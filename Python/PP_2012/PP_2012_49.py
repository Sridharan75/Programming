def fun(a):
    i,c,j=1,a[0],0
    while i<len(a):
        if (a[i]>c):
            c=a[i]
            j=i
        i=i+1
    return j
print(fun([5,2,23,10,-3]))
