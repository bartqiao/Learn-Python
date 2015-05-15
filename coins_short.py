# coins_short.py
# ask user input how many coins they have for different types of coins.

n = int(input('How many nickles: '))
d = int(input('How many dimes: '))
q = int(input('How many quarters: '))

#calculate the number of coins and total amount of the coins.
total_coins = n + d + q
total_amount = 5 * n + 10 * d + 25 * q

#print the result
print()
print('There is total ' + str(total_coins) + ' I have')
print('The total amount of coins is ' + str(total_amount) + ' cents.')
