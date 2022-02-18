def navo_greet():
    print("Hello *Hanshika*!")


def sri_greet():
    print("Hello *Anirudh*!")


def greet(pname):
    print(f"Hi {pname}")


# def wish()
#print("How are you?")


name = input("Enter your name: ")
if name == "Sri" and "sri" and "Sritharan" and "sritharan" and "Sridharan" and "sridharan":
    sri_greet()
elif name == "Navo" and "Navoda" and "Navoda madushika" and "navoda" and "navo":
    navo_greet()
else:
    greet(name)
