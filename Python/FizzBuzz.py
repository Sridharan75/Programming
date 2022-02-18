number = int(input("Enter a number : "))
if(number % 5 == 0) & (number % 3 == 0):
    print("FizzBuzz")
elif(number % 5 == 0):
    print("Fizz")
elif(number % 3 == 0):
    print("Buzz")
else:
    print(number)
