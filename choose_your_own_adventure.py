name=input("Type your Name: ")
print("Welcome",name,"to this adventure!")

answer=input("You are on Dirt road, it has come to end and you can go left or right. Which way would you like to go? ").lower()

if answer=="left":
    answer=input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swin across: ").lower()
    if answer=="swim":
        print("You tried to swim across the river and was eaten by alligator.You died!")
    elif answer=="walk":
        print("You walked many miles, ran out of water and died due to dehydration.")     
    else:
        print("Not a valid option. You lose")
        
elif answer=="right":
    answer=input("You come to a bridege, it looks wobbly, do you want cross it or head back (cross/back)?").lower()
    if answer=="back":
        print("You choose to head back and you lose.")
    elif answer=="cross":
        answer=input("You cross the bridge and met a stranger . Do you want to talk to them(yes/no)?").lower()
        if answer=="yes":
            print("You talked to stranger and he gave you the map for the treassure but some part of the map is gone.")
            answer=input("Now to reached the the place where the part of the map is not available.\nThere are three ways going in front of you (straight/right/left)choose one:").lower()
            if answer=="right":
                print("You Lose!!!")
            elif answer=="left":
                print("You Lose!!!")
            elif answer=="straight":
                print("You picked the right path and you got into an village.")
                answer=input("You found an empty well. Decide whether to go inside or not to (go/not to go)").lower()
                if answer=="go":
                    print("You found a chest and opend it. YOU WIN!!! You got GOLD COINS WORTH 10 Million dollars!!!")
                elif answer=="not to go":
                    print("You decided not to go inside the well and all the efforts you took to reach here gone WASTE!!! YOU LOST!!")
                else:
                    print("Not an valid option.You lose!!!")
            else:
                print("Not an valid option!!")
            
        elif answer=="no":
            print("You decide not to talk to them and to lost the Game!!!")
        else:
            print("Not an valid option!!")
else:
    print("Not a valid option. You lose.")