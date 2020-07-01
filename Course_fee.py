
course_fee=int(input("Enter your course fee "))
number=int(input("Enter your score "))
branch=input("Enter your branch name [Engineering/Arts] ")
scholarship=[0,0]

if branch=='Engineering':
    if number in range(86,101):
        scholarship[0]=0.5
    elif number%7==0:
        scholarship[1]=0.05

if branch=='Arts':
    if number in range(90,101):
        scholarship[0]=0.5
    elif number%2!=0:
        scholarship[1]=0.05

scholarship=max(scholarship)
scholarship_fee=course_fee*scholarship
final_fee=(course_fee-scholarship_fee)

print("In",branch,"Your total course fee is",final_fee)
