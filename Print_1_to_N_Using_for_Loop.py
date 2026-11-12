"""
Pass -1 as the third argument to range() so Python counts backward from 1 down to n.
"""

try:
    n = int(input("Enter a number : "))

    if n > 0:
        for i in range(1, n+1):
            print(i)

    else:
        for i in range(1, n-1,-1):
            print(i)

except ValueError:
    print("Please enter number only")
