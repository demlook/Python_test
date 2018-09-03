print("what's your favorite number?")
num = input()
print("can you guess the number?")
guessnum = input()
while guessnum != num:
    if guessnum > num:
        print("wrong number is bigger,please guess it again!")

    if guessnum < num:  
        print("wrong number is lower,please guess it again!")

if guessnum == num:
        print("congratulations!")

