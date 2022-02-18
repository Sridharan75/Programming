num=[1,2,3,4,5]
find=int(input("number you want to find: "))
for i in num:
    if find==i:
        print("Yes -found")
        break
else:
    print("No -not found")
