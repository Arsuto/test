#keep_going = 'y'
#while keep_going == 'y':
#    sales = float(input('Enter the amount of sales : '))
#    comm_rate = float(input('Enter the commission rate :'))
#    commission = sales*comm_rate
#    print (f'The commission is ${commission:.2f}')
#    keep_going = input('Do you want to calcurate another' + ' commission (Enter y for yes): ')

#keep_going = 'y'
#while keep_going == 'y':
#    cost = float(input('Enter the item another wholesale cost : '))
#    price = cost * 2.5
#    print (f'Retail price: ${price:.2f}')
#    keep_going = input('Do you have another item? (Enter y for yes): ')

#num_rows = int(input('How many row? : '))
#num_columns = int(input('How many columns? : '))
#for i in range(num_rows):
#    for j in range(num_columns):
#        print("*" ,end="")
#    print()

import random
print("What is my magic number (1 to 100) ?")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber :
    msg = str(ntries) + " >> "
    if (ntries == 6):
        print("Your last chance")
    yourguess = int(input(msg))
    if yourguess > mynumber:
        print("---> Too High")
    else:
        print("---> Too Low")
    ntries += 1

if yourguess == mynumber :
    print("Yes! it's ", mynumber)
else:
    print("Sorry! my number is ", mynumber)