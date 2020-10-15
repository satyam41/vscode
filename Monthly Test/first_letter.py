def name_of_first_letter(name, surname):
    firstchar = name[0]
    surfirstchar = surname[0]
    return firstchar, surfirstchar

if __name__ == "__main__":
    name = "Satyam"
    surname = "Krishna"
    print(f"Your first name and second name of first letter is {name_of_first_letter(name,surname)} and your name is {name} {surname}")
