try:
    num = int(input("Enter number : "))
    if num % 2 == 0:
        print(f"The number {num} is Even")
    else:
        print(f"The number {num} is Odd")

except ValueError:
    print("Please enter a number only. Whatever shit you just typed is not a number !")

