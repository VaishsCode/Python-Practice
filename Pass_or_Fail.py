try:
    num = int(input("Enter you marks : "))
    if num >= 40:
        print("CONGO Bro, You have passed !")
    else:
        print("Tsk Tsk , You have failed !")

except ValueError:
    print("Are you sure you are entering your right marks , Please enter marks in number only !")