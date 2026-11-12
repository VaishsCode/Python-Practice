try:
    n = int(input("Enter a number : "))
    i = 1
    if n > 0:
        while i <= n:
            print(i)
            i = i + 1

    else:
        while i >= n:
            print(i)
            i = i - 1

except ValueError:
    print("Please enter a number only !")
