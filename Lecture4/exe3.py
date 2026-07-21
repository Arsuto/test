num_rows = 100
print('You got 100 rows')
num_columns = int(input('How many columns do u want? : '))
for i in range(num_rows):
    for j in range(num_columns):
        print("*" ,end="")
    print()


print_colum = int(input("Enter the number of colums : "))
for i in range (1,101):
    print(f"{i:>3}", end=" ")
    if i % print_colum == 0:
        print ()

