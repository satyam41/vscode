def name_of_first_letter(name, surname):
    firstchar = name[0]
    surfirstchar = surname[0]
    return firstchar, surfirstchar

if __name__ == "__main__":
    name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    print(f"Your first name and second name of first letter is {name_of_first_letter(name,surname)} and your name is {name} {surname}")
