  
while True:
    print("Hello world, this calculator is code 1152095")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))  

    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    option = int(input("indicate the number of operation you want to perform:"))

    if option == 5:
        print("CASIO OFF")
        break
    if option == 1:
        print("Result:", num1, "+" , num2, "=" , num1+num2)
    elif option == 2:
        print("Result:", num1, "-" , num2, "=" , num1-num2)
    elif option == 3:
        print("Result:", num1, "*" , num2, "=" , num1*num2)
    elif option == 4:
        if num2 != 0:
            print("Result:", num1, "/", num2, "=", num1 / num2)
        else:
            print("Division by zero is not allowed")
    else:
        print("Invalid option")
