num=int(input('Enter a num: '))
while num!=0:
    reminder=""
    while num>0:
        reminder=reminder+str(num%2)
        quad=num//2
        if quad==0:
            break
        num=quad
    print(reminder[::-1])
    num=int(input('Enter a num: '))
