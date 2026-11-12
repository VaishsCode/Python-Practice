try:
    num = int(input("Enter a number : "))
    if num % 5 == 0:
        print(f"The number {num} is divisible by 5 !")
    else:
        print(f"Nahhh ! , the number {num} is not divisible by 5 !")

except ValueError:
    print("Please enter number only !")
