num=int(input('Enter a num: '))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,' is not prime')
            print(i,'time',num//i,"=",num)
            break
    else:
        print(num,'prime num')
else:
    print("not a prime number values for negative integers")
