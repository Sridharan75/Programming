while True:
    try:
        units=int(input("Enter Units of used: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        
charge=0
if (units<0):
    print("Oops!  That was no valid number.  Try again...")
elif (units<=120):
    charge=units*5.45
elif(units<=240):
    charge=654+(units-120)*6.7
else:
    charge=654+804+(units-240)*7.7
print("Units you used ",units)
print("Dear cutomer your this month charge is ",charge)
