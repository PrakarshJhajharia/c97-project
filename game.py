import random
a = int(input("Pls guess a number between 1 and 9 : "))
b = random.randint(0, 9)
c = 0
for i in range(5,1,-1):
    if (a == b):
        print("Congrats! you won")
        c = 1
        i = 0
        break;
        
        
    elif a>b:
        print("Your guess was too high. Guess a number lower than ",a)
        a = int(input("Your guess : "))
    elif a<b:
        print("Your guess was too low. Guess a number higher than ",a)
        a = int(input("Your guess : "))
if (a == b and c == 0):
        print("Congrats! you won")
        i = 1
if i == 2:
    print("you loose")

