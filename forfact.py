__author__ = 'Bart Qiao'
n = int(input('Enter an integer number, it should >= 0: '))
fact = 1
for i in range(2, n + 1):
    fact = fact * i
print(str(n) + ' factorials is ' + str(fact))
