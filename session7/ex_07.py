# create a function that checks if fermats princple is correnct for values greater than 2 for n
# it should contain 4 paramters
# it should also print  "holy smokes , fermat was wrong" if hes wrong and " no, that doesnt work"

from turtle import window_height


def check_fermat(a, b, c, n):
    """this function will take any integer values for a b c and n and will check if fermats is right """
    if (a**n)+(b**n) == c**n and n < 2:
        print('Holy somkes, Fermat is wrong')
    else:
        print("no that doesnt work")


# check_fermat(1, 1, 2, 4)
# create function that asks for inputs for each variable, from there input those variables into check fermat function


def prompt():
    """this function will request inputs from the user for inputs for the check_fermat """
    a = int(input("give me an input for a"))
    b = int(input("give me an input for b"))
    c = int(input("give me an input for c"))
    n = int(input("give me an input for n"))
    check_fermat(a, b, c, n)
# prompt()

# excersie two, claculate bmi function and conversion


def calculate_bmi(weight, height):
    """this function will take 2 parameters and calculate BMI from weight and height which are the parameters"""
    return (weight/height**2)*703
# print(calculate_bmi(220, 72))


def get_bmi_category():
    """this function will take the bmi value and give it the correct category that is attributed to the value"""
    weight = float(input("give me a weight: "))
    height = float(input("give me a height: "))
    bmi = calculate_bmi(weight, height)
    if bmi < 18.5:
        return f"the BMI Category is:{bmi}, this is underweight"
    elif bmi < 24.5:
        return f"the BMI Category is:{bmi}, this is normal weight"
    elif bmi < 29.9:
        return f"the BMI Category is:{bmi}, this is overweight"
    else:
        return f"the BMI Category is:{bmi}, this is Obesity"


print(get_bmi_category())
