# Summing number

string = input('Enter a number for summing (or done when finished): ')
total = 0
while string != 'done':
    number = int(string)
    total = total + number
    string = input('Enter a number for summing (or done when finished): ')
print('Total number is: ' + str(total))

