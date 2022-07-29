import random
print("Welcome to Guess Number game")
value=random.randint(1, 100)
print(value)
n=None
i=1
while n!=value and i!=6:
    n=int(input("please guess a number between 1 and 100:   "))
    if n>value:
        print("chance "+str(i)+" please guess lower value")
        print("try again")
    elif n<value:
        print("chance "+str(i)+" please guess greater value")
        print("try again")
    i=i+1
if(i<=5 and n==value):
    print("you won")
else:
    print("you lose")