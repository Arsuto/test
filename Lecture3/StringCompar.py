String1 = "Mary" 
String2 = "Mark"

if String1 == String2:
    print(f'"{String1}" and "{String2}" are equal.')
else:
    print(f'"{String1}" and "{String2}" are not equal.')


if String1 < String2:
    print(f'"{String1}" comes befores "{String2}" in lexicograpical order.')
else:
    print(f'"{String1}" comes afters "{String2}" in lexicograpical order.')


if String1.lower() == String2.lower():
    print(f'"{String1}" and "{String2}" are equal when case is ignored.')
else:
    print(f'"{String1}" and "{String2}" are not equal when case is ignored.')

