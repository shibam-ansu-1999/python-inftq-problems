def palin(text):
    if len(text)<=1:
        print("Palindrome")
    else:
        if text[0]==text[-1]:
            #print(text[1:-1])
            palin(text[1:-1])

        else:
            print("Not a palindrome")

string=input("Enter the string to Check: ")
palin(string)
