def add():
    while True:
        try:
            a = int(input("Enter first number : ").strip())
            b = int(input("Enter second number : ").strip())
        except ValueError:
            print("Please enter whole numbers only")
            continue
        break
    print("Sum =", a + b)

add()