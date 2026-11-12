try:
    num = int(input("Enter a number : "))

    if num > 0:
        print(f"The number {num} is positive number !")
    else:
        if num < 0:
            print(f"The number {num} is negative number !")
        else:
            print("The number is Zero !")

except ValueError:
    print("Please enter a number only. Whatever shit you just typed is not a number !")
