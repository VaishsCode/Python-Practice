def welcome():
    while True:
        name = input("Enter student name : ").strip()
        if name == "":
            print("Name cannot be empty")
            continue
        break
    print("Welcome", name, "to Machine Learning")

welcome()