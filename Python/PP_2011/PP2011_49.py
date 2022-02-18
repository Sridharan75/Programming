data = [5,1,23,10,-3]
def fun(a):
    i,c = 1, a[0]
    while i< len(a):
        if (a[i]>c):
            c=a[i]
        i=i+1
    return c
print(fun(data))
