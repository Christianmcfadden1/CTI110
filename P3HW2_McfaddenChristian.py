
# CTI-110
# P3HW2 - Pizza Order
# Christian Mcfadden 
# 3-11-2022
#

student_te = int(input("How many students do you want to order pizza for? "))
pizza_pp = float(input("Enter number of people per pizza ( 1.5, 2 or 3): "))

def main():

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
    else:
            print("INVALID ENTRY!!!!")
            print("Should have entered 1.5, 2, or 3")
            print("Run Program again")



main()


