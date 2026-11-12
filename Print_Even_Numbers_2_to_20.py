"""
The 'continue' keyword tells Python to immediately jump back to the top of the while loop,
skipping i = i + 1 at the bottom.
Because i stays stuck at 3, the loop repeats endlessly without printing anything new.

"""

i = 2

while i <= 20:
    if i % 2 == 0:
        print(i)
    #else:
        #continue

    i = i + 1
