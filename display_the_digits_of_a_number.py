try:
    num = int(input("Enter a number : "))
    digits = []

    n = num

    while num > 0:
        digits.append(num % 10)
        num = num // 10

    print(f"The digits of number {n} are ->")

    for i in reversed(digits):
        print(i)


except ValueError:
    print("Please enter number only !")
