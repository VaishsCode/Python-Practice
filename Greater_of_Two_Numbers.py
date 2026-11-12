try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    if num1 > num2:
        print(f"The first number {num1} is greater than second number {num2} !")
    elif num2 > num1:
        print(f"The second number {num2} is greater than first number {num1} !")
    else:
        print("The numbers are equal !")

except ValueError:
    print("Please enter number only !")
