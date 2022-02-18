alphabets = {"A":1,"I":1,"J":1,"Q":1,"Y":1,"B":2,"K":2,"R":2,"C":3,"G":3,"L":3,"S":3,"D":4,"M":4,"T":4,"H":5,"E":5,"N":5,"X":5,"U":6,"V":6,"W":6,"O":7,"Z":7,"P":8,"F":8}

word =input("your numerology score is :") #since i am using python 3 to code this

def digit_sum(n):
    #prepare a list of numbers in n convert to string and reconvert
    numbers=[]
    for digit in str(n):
        numbers.append(int(digit))
    # add up the total of numbers    
    total=0
    for number in numbers:
        total += number
    return total  

def numerology(word):
        total = 0
        for letter in word.upper():
            total += alphabets[letter]
            total = digit_sum(total)

        return total

print (numerology(word))
