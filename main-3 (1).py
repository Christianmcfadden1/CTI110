user_input = str(input("Enter desired auto service "))

print("You entered: " + user_input + " ") 

if user_input == "oil change":
    print("Cost of oil change: $35")
    if user_input == "Tire rotation":
        print("Cost of tire rotation: $19")
        if user_input == "car wash":
            print("Cost of car wash: $7")
        else:
            print("Error: Requested service is not recognized")


    

