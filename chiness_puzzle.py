import math
head_count=int(input("Enter the number of head: "))
leg_count=int(input("Enter the number of legs: "))

rabit=0.5*leg_count-head_count

if math.ceil(rabit)==math.floor(rabit):

    rabit=int(rabit)
    chiken=head_count-rabit
    print("Number of chiken:",chiken,"Number of rabit:",rabit)
else:
    print("No solution")

