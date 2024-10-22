print("Welcome to treasure island\n""your mission is to find the treasure.")
a= input("left of right ")
if a=='right':
    print("game over")
else:
    b= input("swim or wait")
    if b=="swim":
        print("Game Over")
    else:
        print("red , blue , yellow")
        c= input("Which door")
        if(c=="yellow"):
            print("You win")
        else:
            print("Game over")
