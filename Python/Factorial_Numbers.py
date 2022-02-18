n = int(input("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range (1,(n+1)):
       factorial = factorial * i
    print("Factorial of ",n , " is : ",factorial)
elif n==0:
    print("Factorial of 0 is : 1")
else:
    print("Sorry, factorial does not exist for negative numbers")
