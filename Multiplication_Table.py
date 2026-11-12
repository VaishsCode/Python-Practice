try:
    num = int(input("Enter a number : "))
    i = 1

    while i <= 10:
        print(f"{i} X {num} = {i*num}")
        i = i + 1

except ValueError:
    print("The thing you are typing is not a number, please enter number only !")
