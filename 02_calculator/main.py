operator = input("Enter operator:")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
if operator == "+": print("Result:", num1 + num2)
elif operator == "-": print("Result:", num1-num2)
elif operator == "*": print("Result:", num1*num2)
elif operator == "/":
    if  num2 != 0: print("Result:", num1/num2)
    else: print("Cannot divide by zero")
else: print ("Invalid operator")
    


    # answer = "yes" 
    # while answer == "yes": 
    #     operator = input("Enter operator:")
    #     num1 = float(input("Enter first number:"))
    #     num2 = float(input("Enter second number:"))
    #     if operator == "+": print("Result:", num1 + num2)
    #     elif operator == "-": print("Result:", num1-num2)
    #     elif operator == "*": print("Result:", num1*num2)
    #     elif operator == "/":
    #         if  num2 != 0: print("Result:", num1/num2)
    #         else: print("Cannot divide by zero")
    #     else: print ("Invalid operator")
    #     answer = input("Do you want to continue? (yes/no):")