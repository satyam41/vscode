# Write a short program that ask for your height in centimeters and then converts your height to feet and inches.(1foot = 12inches, 1inch = 2.54cm)

def HeightConverter(height):
    print(f"Your height in centimeter {height}cm.")
    heightInInch = height / 2.54
    print(f"Your height in inch {heightInInch}inch.")
    heightInfeet = heightInInch / 12
    print(f"Your height in foot {heightInfeet}feet.")


HeightConverter(162)
