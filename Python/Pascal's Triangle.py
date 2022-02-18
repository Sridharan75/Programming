n=5
for line in range(1, n + 1):
    coef = 1  
    for i in range(1, line + 1):   
        print(coef, end = " ") 
        coef= int(coef * (line - i) / i)
    print("\n")
