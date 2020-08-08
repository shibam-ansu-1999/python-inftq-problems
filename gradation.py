number=int(input("Enter the achieved number: "))

if number in range(80,101):
    print("Grade is A")
elif number in range(73,80):
    print("Grade is B")
elif number in range(65,73):
    print("Grade is C")
elif number in range(0,65):
    print("Grade is D")
else:
    print("Grade is Z")
