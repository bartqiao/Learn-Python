__author__ = 'Bart Qiao'
n = int(input('Enter an integer number, it should be >= 0: '))
fact = 1
i = 2
while i <= n:
    fact = fact * i
    i = i + 1
    print(str(n) + ' factorials is ' + str(fact))
print(str(n) + ' factorials is ' + str(fact))
