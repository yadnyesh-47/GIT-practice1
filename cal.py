def addition(a,b):
    add= a + b
    return add

def substraction(a,b):
    sub = a - b
    return sub



a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

sum = addition(a,b)
print(f"Sum is : {sum}")

diff = substraction(a,b)
print(f"Difference is : {diff}")