"""num = 2
count = 0
while num<10:
    count += 1
    print(num)
    num += 2
print(f"We have {count} even numbers")
"""
count=0
for number in range(1,10):
    if (number%2==0):
        print(number)
        count+=1
print(f"We have {count} even numbers")
