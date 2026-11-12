try:
    n = int(input("Enter a number : "))

    i = 1
    

    if n > 0:
        sum = 0
        while i <= n:
            sum = sum + i
            i = i + 1

    else:
        sum = 0
        while i >= n:
            sum = sum + i
            i = i - 1

    print(f"The sum of numbers form 1 to {n} is : {sum}")


except ValueError:
    print("Please enter value only !")
