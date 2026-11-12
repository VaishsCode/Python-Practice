num = []

print("Enter whole numbers in list , and type 'done' to finish ")

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


"""Accessing using positive indexing"""

i = 0
print("\nAccessing using positive indexing")
while i < len(num):
    print(num[i])
    i = i + 1

print("-" * 50)

"""Accessing using negative indexing"""

i = -1
print("\nAccessing using negative indexing")
while i >= -len(num):
    print(num[i])
    i = i - 1
