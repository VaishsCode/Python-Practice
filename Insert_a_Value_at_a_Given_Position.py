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


print("Current list:", num)


while True:
    try:
        inx = int(input("Enter a position at which you want to insert a value : "))
    except ValueError:
        print("Please enter a number only")
        continue

    if inx < 0 or inx > len(num):
        print("Position must be between 0 and", len(num))
        continue

    break


while True:
    try:
        value = int(input("Enter a value you want to insert : "))
    except ValueError:
        print("Please enter a whole number only")
        continue

    break

num.insert(inx, value)
print("List after insertion:", num)
