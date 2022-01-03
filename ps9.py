
# number guessing game 

import random

random_number = random.randint(1,10)
guess = None

while guess!= random_number:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess< random_number:
        print("TOO LOW")
    elif guess > random_number:
        print("TOO HIGH")
    else:
        print("YOU WON")



# Snake water gun game  

import random

def gameWin(comp,you):

    if (comp==you):
        return None
    
    elif comp=="s":
        if you == "w":
            return False
        elif you == "g":
            return True
    
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

print("Comp Turn :Choose Snake(s) Water(w) or Gun(g)??? ")

random_no = random.randint(1,3)

if random_no == 1:
    comp = 's'
elif random_no == 2:
    comp = 'w'
elif random_no == 3:
    comp = 'g'

you = input("Your Turn : Choose Snake(s) Water(w) or Gun(g)???" )
a =gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You Chose {you}")

if a==None:
    print("The Game is a Tie....")
elif a==True:
    print("You Win!!!")
elif a==False:
    print("You Lose!!!")
    