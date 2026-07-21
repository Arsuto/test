input_string = input("enter a string: ")
modified_string = ""
Vowels = "aeiouAEIOU"
for char in input_string:
    upper_char = char.upper()
    if upper_char in Vowels:
        modified_string += "*"
    else:
        modified_string += upper_char

print("Modified String: ",modified_string)


