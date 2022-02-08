"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""
# create input for your user to input a weight
# create a function that will turn that into a moonweight
# print that moon weight

weight = int(
    input(" give me a weight and ill tell you what it weighs on the moon!:"))


def moonweight(weight):
    """this function will take a weight on from the earth in the value of an integer and will convert it to a moon weight by multiplying by a constant"""
    newweight = weight*.165
    return newweight


print(moonweight(weight))
