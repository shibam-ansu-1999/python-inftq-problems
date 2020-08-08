import random

jackpot=random.randint(1,100)
#print(jackpot)
guess=int(input("Guess the number"))
counter=1
while guess!=jackpot:
    counter=counter+1
    if guess<jackpot:
        print("Wrong.Guess Higher")
        guess=int(input("Guess the number again"))
    else:
        print("Wrong.Guess Lower")
        guess=int(input("Guess the number again"))

print("Right guess")
print("you took",counter,"attmeps")
    
    

