num_employees = int(input("Enter the number of employees: "))

if num_employees < 50:
    print("This is small company.")
elif num_employees < 250:
     print("This is medium-sized company.")
else:
     print("This is large company.")