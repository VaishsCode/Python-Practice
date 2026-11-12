numbers = []

print("Enter 5 whole numbers")

while len(numbers) < 5:
    value = input("Enter number " + str(len(numbers) + 1) + " : ").strip()

    try:
        numbers.append(int(value))
    except ValueError:
        print("Please enter a whole number only")

print("-" * 50)

count = 0

for n in numbers:
    if n % 2 == 0:
        print(n)
        count = count + 1

print("Even count =", count)