num = []

print("Enter whole numbers in list and type 'done' when you want to finish")

while True:

    number = input("Enter a number : ").strip()
    if number.lower() == "done":
        break

    try:
        num.append(int(number))

    except ValueError:
        print(
            "Please enter either a whole number or type 'done' correctly to finish typing "
        )


print("-" * 50)

i = 0

print(f"The numbers in list are : {num} ")
