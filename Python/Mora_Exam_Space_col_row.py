for row in range(1,3):
    for col in range(1,3):
        prod=row*col
    if prod<10:
        print("*",end=" ")
    print(row*col,"-",end=" ")
print()
