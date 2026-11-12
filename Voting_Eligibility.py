try:
    age = int(input("Enter you age : "))
    if age < 0:
        print("Typing from womb ? Please enter a real age!")
    elif age >= 18:
        print("YES ! You can vote ! so be mindful about it ")
    else:
        print("Nahhh , you are still a kid for democracy !")

except ValueError:
    print("Please enter valid age !");