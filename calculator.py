print("Simple Calculator \nEnter Any Number you want to apply arthamatic operation\nyou can enter only two numbers ")
num1 = float(input("Enter Number1: "))
opr = input("Enter Arthamatic Operation: ")
num2 = float(input("Enter Number2: "))
mul = ("*")
add = ("+")
sub = ("-")
div = ("/")
if opr == add:
    print(num1 + num2)
elif opr == sub:
    print(num1 - num2)
elif opr == mul:
    print(num1 * num2)
elif opr == div:
    print(num1 / num2)
else :
    print("Wrong Operation ")