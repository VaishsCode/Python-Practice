try:
    n = int(input("Enter a number : "))

    if n > 0:
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i)

    else:
        for i in range(1, n - 1,-1):
            if i % 2 == 0:
                print(i)

except ValueError:
    print("Please enter number only")
