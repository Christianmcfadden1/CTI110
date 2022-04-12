# 2-22-22
# CTI-110 P2HW1 - Total Purchases
# Christian Mcfadden
# This program calculates the price of the items and their tax

#get input for item1-item4
item1 = float(input("Enter item one price: "))
item2 = float(input("Enter item two price: "))
item3 = float(input("Enter item three price: "))
item4 = float(input("Enter item four price: "))
item5 = float(input("Enter item five price: "))

#calculate subtotal tax and overall total
subtotal = item1 + item2 + item3 + item4 + item5

tax = subtotal * 0.07

overall_total = subtotal + tax

#display all three variables
print('---------------------')
print('Subtotal: $', format(subtotal, '.2f'), sep='')
print('Tax: $', format(tax, '.2f'), sep='')
print('Overall Total: $', format(subtotal, '.2f'), sep='')
print('---------------------')
