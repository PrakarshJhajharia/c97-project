import random
a = int(input("Pls guess a number between 1 and 9 : "))
b = random.randint(0, 9)
for i in range(101,1,-1):
    if (a == b):
        print("Congrats! you won")
        break;
    elif a>b:
        print("Your guess was too high. Guess a number lower than ",a)
        a = int(input("Your guess"))
    elif a<b:
        print("Your guess was too low. Guess a number higher than ",a)
        a = int(input("Your guess"))

