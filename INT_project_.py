import random
min=1
max=6
score=0

while True:
    static=int(input("Enter a static number:"))
    if static>=min and static<=max:
    
        rolldice=random.randint(min,max)
        print(rolldice)
        if rolldice==static:
            print("You won the game!")
            score=score+5
        else:
            print("You loose the game!")
    else:
         print("Wrong Number Entered.")
    user_confirmation=input("Do you want to paly again?Press yes/no:")
    if user_confirmation.lower()=="yes":
            continue
    else:
        print("You exit the game.")
        break
print("The final score is:",score)





    



