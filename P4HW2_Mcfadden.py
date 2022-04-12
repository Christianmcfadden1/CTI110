
# CTI-110
# P3HW2 - Pizza Order
# Christian Mcfadden 
# 3-11-2022
#


def main():
    student_te = int(input("How many students do you want to order pizza for? "))
    pizza_pp = float(input("Enter number of people per pizza ( 1.5, 2 or 3): "))

    if pizza_pp == 1.5:
        tax = 0.06
        pizza = 5
        pizza_needed = student_te / pizza_pp
        price = pizza_needed * pizza
        price = (price * tax) + price
        print("---------Pizza Order-----------")
        print("Number of Students: ", student_te)
        print("Pizzas Needed: ", round(pizza_needed))
        print("Price $" + str(price))
        print("-----------------------------")
        answer = input("Would you like to run program again(y for yes): ")
        if answer == "y":
            del pizza_pp
            del student_te
            main()
        else:
            print("Program has ended")
    elif pizza_pp == 2:
        tax = 0.06
        pizza = 5
        pizza_needed = student_te / pizza_pp
        price = pizza_needed * pizza
        price = (price * tax) + price
        print("---------Pizza Order-----------")
        print("Number of Students: ", student_te)
        print("Pizzas Needed: ", round(pizza_needed))
        print("Price $" + str(price))
        print("-----------------------------")
        answer = input("Would you like to run program again(y for yes): ")
        if answer == "y":
            del pizza_pp
            del student_te
            main()
        else:
            print("Program has ended")
    elif pizza_pp == 3:
        tax = 0.06
        pizza = 5
        pizza_needed = student_te / pizza_pp
        price = pizza_needed * pizza
        price = (price * tax) + price
        print("---------Pizza Order-----------")
        print("Number of Students: ", student_te)
        print("Pizzas Needed: ", round(pizza_needed))
        print("Price $" + str(price))
        print("-----------------------------")
        answer = input("Would you like to run program again(y for yes): ")
        if answer == 'y':
            del pizza_pp
            del student_te
            main()
        else:
            print("Program has ended")
    else:
        print("INVALID ENTRY!!!!")
        print("Should have entered 1.5, 2, or 3")
        del pizza_pp
        del student_te
        second()

        
def second():
    student_te = int(input("How many students do you want to order pizza for? "))
    pizza_ap = float(input("Enter number of people per pizza ( 1.5, 2 or 3): "))
    

    if pizza_ap == 1.5:
        tax = 0.06
        pizza = 5
        pizza_needed = student_te / pizza_ap
        price = pizza_needed * pizza
        price = (price * tax) + price
        print("---------Pizza Order-----------")
        print("Number of Students: ", student_te)
        print("Pizzas Needed: ", round(pizza_needed))
        print("Price $" + str(price))
        print("-----------------------------")
        answer = input("Would you like to run program again(y for yes): ")
        if answer == "y":
            del pizza_ap
            del student_te
            main()
        else:
            print("Program has ended")
    elif pizza_ap == 2:
        tax = 0.06
        pizza = 5
        pizza_needed = student_te / pizza_ap
        price = pizza_needed * pizza
        price = (price * tax) + price
        print("---------Pizza Order-----------")
        print("Number of Students: ", student_te)
        print("Pizzas Needed: ", round(pizza_needed))
        print("Price $" + str(price))
        print("-----------------------------")
        answer = input("Would you like to run program again(y for yes): ")
        if answer == "y":
            del pizza_ap
            del student_te
            main()
        else:
            print("Program has ended")
    elif pizza_ap == 3:
        tax = 0.06
        pizza = 5
        pizza_needed = student_te / pizza_ap
        price = pizza_needed * pizza
        price = (price * tax) + price
        print("---------Pizza Order-----------")
        print("Number of Students: ", student_te)
        print("Pizzas Needed: ", round(pizza_needed))
        print("Price $" + str(price))
        print("-----------------------------")
        answer = input("Would you like to run program again(y for yes): ")
        if answer == "y":
            del pizza_ap
            del student_te
            main()
        else:
            print("Program has ended")
    else:
        print("INVALID ENTRY!!!!")
        print("Should have entered 1.5, 2, or 3")
        del pizza_ap
        del student_te
        del pizza_ap
        second()
            


main()


