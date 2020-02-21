import random

def print_intro():
    print("""Welcome to Camel!
    In your desperation, you have stolen a camel to make your way
    across the Mobi desert.
    The locals want their camel back and are chasing you down
    Survive your desert trek and out run the locals    
        """)


def main():
    print_intro()

    oasis = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    drinks_in_canteen = 3
    distance_from_locals = -20
    done = False
    while not done:

        print("""
        A. Drink from the canteen
        B. Ahead moderate speed.
        C. Ahead full speed
        D. Stop for the night
        E. Status check.
        Q. Quit 

        """)
        user_choice = input("What is your choice? " )

        if user_choice == "Q":
            done = True
        
        elif user_choice == "E":
             print ("miles_traveled :", miles_traveled)
             print ("drinks_in_canteen:", drinks_in_canteen)
             print ("the locals are", distance_from_locals, "behind you")
             print ("thirst meter:", thirst)
            
        #stop for the night
        elif user_choice == "D":
           print("The camel is happy") 
           camel_tiredness = 0
           distance_from_locals -= random.randrange(7, 15)
       
        #Ahead full speed
        elif user_choice == "C":
            miles_traveled += random.randrange(10, 20)
            print("miles traveled:", miles_traveled)
            thirst += 1 
            camel_tiredness += random.randrange(1, 3)
            distance_from_locals += random.randrange(7, 15)
        if random.randrange(20) == 0:
                oasis = True
       
        #ahead moderate speed            
        elif user_choice =="B":
            miles_traveled += random.randrange(5, 12)
            print("miles traveled:", miles_traveled)
            camel_tiredness += 1
       
        #drink from the canteen
        elif user_choice =="A":
            print("You take a drink from your canteen")
            drinks_in_canteen -= 1
            thirst = 0

        if miles_traveled == random.randrange(1, 200):
            drinks_in_canteen = 0
            thirst = 0
            camel_tiredness = 0
            print(" You have found an oasis")
        
        if thirst > 4 and thirst <= 6:
            print("you are thirsty")
        
        elif thirst > 6:
            print("You died of thirst")
            done = True
        
        if camel_tiredness > 5 and camel_tiredness <= 8:
            print("Your camel is getting tired")

        elif camel_tiredness > 8:
            print("Your camel is dead")  
            done = True

        if distance_from_locals < 15:
            print("The locals are getting close")
            

        elif distance_from_locals == 0:
            print("You've been caught by the locals!!")
            done = True

        
        elif oasis == True:
            print("You stumble upon an oasis")
            drinks_in_canteen = 3
            thirst = 0
            camel_tiredness = 0

        if miles_traveled == 200:
            print("You won the game!!")

        



if __name__ == '__main__':
    main()