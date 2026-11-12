num = []

print("Enter whole numbers in list and type 'done' when you want to finish")

while True:
    number = input("Enter a number : ").strip()

    if number.lower() == "done":
        break

    try:
        num.append(int(number))

    except ValueError:
        print("Please enter either a number or a 'done' to finish")

print("-" * 50)

"""Iterating using for loop"""

print("Iterating using for loop")

for n in num:
    print(n)
