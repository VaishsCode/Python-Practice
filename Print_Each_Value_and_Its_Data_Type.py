items = []

print("Enter values. Type 'done' to finish")

while True:
    value = input("Enter a value : ").strip()

    if value.lower() == "done":
        break

    if value.lower() == "true":
        items.append(True)
    elif value.lower() == "false":
        items.append(False)
    else:
        try:
            items.append(int(value))
        except ValueError:
            try:
                items.append(float(value))
            except ValueError:
                items.append(value)

print("-" * 50)

for item in items:
    print(item, "->", type(item))