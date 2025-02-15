import random


computer = random.choice([-1,0,1])
youstr = input("enter the choice: ")

youdict = {"s":1 , "w": -1, "g" :0}
you = youdict[youstr]

if you is None:
    print("Invalid choice. Please enter 's', 'w', or 'g'.")
else:
    if computer == you:
        print("Draw")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win")
    else:
        print("You lost")



    
