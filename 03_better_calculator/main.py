def addmultiplenumbers(numbers):
    total = 0
    for n in numbers:
        total = total +n
    return total
def multiplymultiplenumbers(numbers):
    total = 1
    for n in numbers:
        total = total * n
    return total
def isitaninteger(number):
    if type(number) == int:
        return True
    else:
        return False
def isiteven(number):
    if isitaninteger(number) == True and number % 2 == 0: 
        return True
    else:
        return False
    
def main():
    print("Calculator")
    choise = input("Enter the choice (add/multiply/evenorodd/isinteger)")
    if choise == "add":
            nums = input("Enter the numbers to add, separated by comas:")
            numbers = []
            for n in nums.split(","):
                numbers.append(float(n))
            print (addmultiplenumbers(numbers))
    elif choise == "multiply":
            nums = input("Enter the numbers to multiply, separated by comas:")
            numbers = []
            for n in nums.split(","):
                    numbers.append(float(n))
            print(multiplymultiplenumbers(numbers))
    elif choise == "evenorodd":
            num = int(input("Enter the number to check if it's even or odd:"))
            if isiteven(num) == True:
                print("The number is even")
            else: 
                print("The number is odd")
    elif choise == "isinteger":
            num = float(input("Enter the number to check if it's an integer:"))
            if isitaninteger(num) == True:
                print ("The number is an integer")
            else: 
                print ("The number is not an integer")
    else:
            print("Invalid choise")

if __name__ == "__main__":
    main()