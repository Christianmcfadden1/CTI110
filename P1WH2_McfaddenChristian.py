# This program will calculate the amount of pizza slices
# 2-15-2022
# CTI-110 P1HW2 - Pizza Order
# Christian Mcfadden
#

#variables to hold a number of people

people = int(input("How many students do you want to order pizza for?"))

# how many slices needed
slices = people * 3

#how many pizzas needed
pizza = people / 2

#display students pizzas and slices

print("")

print("-----Pizza Order--------------")

print("Number of students entered: ", people)
print("Number of pizza slices needed:", slices)
print("Number of pizzas needed:", pizza)

print("-------------------------------")
