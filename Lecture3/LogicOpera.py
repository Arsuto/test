#logic operators
x = 10 
y = 20
z = 30

if x<y and y<z:
    print("x is less than y and y is less than z.")

if x<y or y>z:
    print("Either x is less than y is greather than z.")

if not (x>y):
    print("x is not greather than y.")
print("-----ends-----")

#identity operators
a= [1,2,3]
b = a
c = [1,2,3]
d = [1,2,3]

print(a is b)
print(a is c)
print(c is d)
print(a == c)
print(c == d)
print("-----ends-----")

#membership opeartors
fruits = ["apple","banana","cherry"]

print("banana" in fruits)
print("orange" in fruits)
print("grape" not in fruits)
print("apple" not in fruits)

sentence = "the quick brow fox jumps over the lazy dog."
print("fox" in sentence)
print("cat" not in sentence)
print("-----ends-----")


#Combine
age = 25
income = 50000
12345678
if age >= 18 and age <=65 and income > 30000:
    print("You are eligible for the loan.")
else:
        print("You are not eligible for the loan.")
