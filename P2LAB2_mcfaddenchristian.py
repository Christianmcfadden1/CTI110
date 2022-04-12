current_price = int(input())
last_months_price = int(input())

difference = current_price - last_months_price

monthly_mortgage = (current_price * 0.051) / 12

print('This house is $' + str(current_price) + '.' + ' The change is $' + str(difference) + ' since last month.')
print('The estimated monthly mortgage is $' f'{monthly_mortgage:.2f}' '.')


   