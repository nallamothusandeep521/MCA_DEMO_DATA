print("Hello, World!")
print(2+2)
print("1"+"1")

print("sandeep"+" sai")

print(10*" sandeep")
#---------------------------------------------------
num1 = float(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2 #-> result = 10 + 20
print("The sum of", num1, "and", num2, "is", result)
#---------------------------------------------------
# if else statement

num1 = int(input("Enter first number: ")) #10
num2 = int(input("Enter second number: ")) #20
if num1 > num2: # 
    print("Big")
else:
    print("Small")
#---------------------------------------------------
vote = int(input("Enter your age: "))
if vote >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")