# """
# Question 1:

# Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

# Weight on Moon = weight on Earth * 0.165

# Notice:
# 1. Please write pseudo-code before coding the function.
# 2. Your function should include docstring.
# 3. Write your own test code, i.e. call the function.
# """
# # create input for your user to input a weight
# # create a function that will turn that into a moonweight
# # print that moon weight

# weight = int(
#     input(" give me a weight and ill tell you what it weighs on the moon!:"))


# def moonweight(weight):
#     """this function will take a weight on from the earth in the value of an integer and will convert it to a moon weight by multiplying by a constant"""
#     newweight = weight*.165
#     return newweight


# print(moonweight(weight))




"""
Question 2:

Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.

Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Jupiter = weight on Earth * 2.528

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""
# make function take 2 parameters weight on eath and planet name in str
# it returns equivielnt weights on both so multiply by constant based on string input
#write docstring and check code

def earthconvert(weight,planet):
    """ this should take in 2 variables and converts earth weights to equivlent weights on different planets"""
    if planet("Jupiter"):
        juipeterweight=weight*2.528
        return juipeterweight
    elif planet("mars"):
        marsweight=weight*.378
        return marsweight
    elif planet("moon"):
        moonweight=weight*.165
        return moonweight
earthconvert(50,'jupiter')
