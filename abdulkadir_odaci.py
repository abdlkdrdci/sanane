print("Hi,you are very welcome to our game")
print("You have 3 items to select : rock,scissors and paper.The game is simple; rock wins scissors, scissors wins paper and paper wins rock.") # simple explanation of the game
import random
score_user= 0
score_computer= 0
while True:  # user can play multiple times thanks to  while
    list=["rock","scissors","paper"] #list of the game items
    items=input("enter your item :")  #users enter their items
    choice_of_computer=random.choice(list)  # computer select rondomly an item
    print("Choice of computer :" + choice_of_computer)  # to see what computer select

    if choice_of_computer=="scissors" and items=="paper":  #all the rules of the game as a code
        score_computer +=1
    elif choice_of_computer=="paper" and items=="scissors":
        score_user +=1
    elif choice_of_computer=="rock" and items=="paper":
        score_user +=1
    elif choice_of_computer=="paper" and items=="rock":
        score_computer +=1
    elif choice_of_computer=="rock" and items=="scissors":
        score_computer +=1
    elif choice_of_computer=="scissors" and items=="rock":
        score_user +=1
    else: # if users selects same item with computer
        print('both side choose the same items , enter your items again !!!')
    print("score of user:", score_user, "score of computer:", score_computer) #to show both side score for each loop
    if score_user==3 or score_computer==3: # to show the game ends who reach 3 point
        break #in order to break loop
if score_user > score_computer: # to show the winner
    print("congratulation, you win !!:)")
else:
    print("you lost the game!! :(" )
