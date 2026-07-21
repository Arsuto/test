numbers = [6,5,3,8,4,2,5,4,11]
sum = 0
for val in numbers:
    sum += val
    print(sum)
print("The sum is", sum)

max = 5
total = 0.0
print('This program calcurates the sum of')
print(max, 'numbers you will enter.')
for counter in range(max):
    number = int(input('Enter a number: '))
    total = total + number
print('The total is ', total)
