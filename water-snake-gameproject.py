import random

# Snake Water Gun   or Rock Paper Sessior
def gameWin(computer, you):
    """This is a snake water gun game not a stone paper  or sessior!"""
    # if two values are equal , declare a tie!
    if computer == you:
        return None
    
    # if (you == "w" and computer == "g") or (you == "g" and computer == "s") or (you == "s" amd computer == "w")
    # return True
    # elif:
    # return False

#Check foe all possiblities when computer choose 's'       
    elif computer == 's':
        if you == 'w':
            return False
        elif you =='g':
            return True

 #Check foe all possiblities when computer choose 'w'
    elif computer =='w':
        if you =='g':
            return False
        elif you == 's':
            return True

#Check foe all possiblities when computer choose 'g'            
    elif computer =='g':
        if you =='s':
            return False
        elif you == 'w':
            return True
         


print("computer turn : snake water or gun?")
randNo = random.randint(1, 3)            #random is a module in python and randint is a function under random module!

if randNo == 1:                         # Declaration 1,2,3 means!
    computer = 's'
elif randNo == 2:
    computer = 'w'
elif randNo == 3:
    computer = 'g'
    
you = input("your turn : Snake{S} Water{w} or Gun{G}? = ")

a = gameWin(computer, you)           # function call                # gameWin is function

print(f"Computer choose =  {computer}")
print(f"you choose = {you}")

if a == None:                         # Announcement!
    print("The Game is tie vibhor!\U0001F610")
elif a:
    print(" vibhor You are winner!\U0001F600")
else:
    print("vibhor Oops! You lose!\U0001F62D")
    
# print(gameWin.__doc__) 
        
 
                                      #Game Statregy


    # 1= Import module
    # 2= made function
    # 3= possiblities and module use
    # 4= Declaration
    # 5= print choose
    # 6= Announcement