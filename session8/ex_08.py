# excercise 1

# #Calculate the sum of integers from 1 to 10.


# def sumofrange(number):
#     """this function will take any positive number and sum all ints from 1 to that number"""
#     sumtotal = 1
#     for i in range(number):
#         i += 1
#         sumtotal += i
#     return sumtotal
# # print(sumofrange(10))
# # Calculate the sum of integers from 1 to 1000. (hint: we need to use range().)
# # print(sumofrange(1000))
# # Calculate the sum of all the odd numbers from 1 to 1000. (hint: check out range() function in Python documentation.) How about all the even numbers?


# def sumofrangeodd(number):
#     """this function will take any positive number and find the sum of all odd integers from one to that number"""
#     sumtotal = 1
#     for i in range(number):
#         if i % 2 == 1:
#             i += 1
#             sumtotal += i
#     return sumtotal
# # print(sumofrangeodd(1000))
# # excercise 2

# # read the following code and answer the questions.

# # iteration = 0
# # count = 0
# # while iteration < 5:
# #     # the variable 'letter' in the loop stands for every
# #     # character, including spaces and commas!
# #     for letter in "hello, world":
# #         count += 1
# #     print("Iteration " + str(iteration) + "; count is: " + str(count))
# #     iteration += 1


# # 1. What is the value of the variable count that is printed out (at the print statement) on iteration 0?
# 12
# # 2. What is the value of the variable count that is printed out (at the print statement) on iteration 1?
# 24
# # 3. What is the value of the variable count that is printed out (at the print statement) on iteration 2?
# 36
# # 4. What is the value of the variable count that is printed out (at the print statement) on iteration 3?
# 48
# # 5. What is the value of the variable count that is printed out (at the print statement) on iteration 4?
# 60

# # iteration = 0
# # while iteration < 5:
# #     count = 0
# #     for letter in "hello, world":
# #         count += 1
# #     print("Iteration " + str(iteration) + "; count is: " + str(count))
# #     iteration += 1
# # 1. What is the value of the variable count that is printed out (at the print statement) on iteration 0?
# 12
# # 2. What is the value of the variable count that is printed out (at the print statement) on iteration 1?
# 12
# # 3. What is the value of the variable count that is printed out (at the print statement) on iteration 2?
# 12
# # 4. What is the value of the variable count that is printed out (at the print statement) on iteration 3?
# 12
# # 5. What is the value of the variable count that is printed out (at the print statement) on iteration 4?
# 12

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1
# 1. How many times will the print statement be executed?
4
# 2. What is the largest value of the variable iteration that will be printed out (at the print statement)?
4
# 3. What is the largest value of the variable count that will be printed out (at the print statement)?
12
# 4. What is the smallest value of the variable count that will be printed out (at the print statement)?
1

#excercise 3 
import math
def mysqrt(a):
    x=a+2
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < .0001:
            break
        x=y
# mysqrt(9)
def test_square_root(n): 
    print ("{:<5} {:<10} {:<15} {:<10}".format('a','mysqrt','math.sqrt','diff'))
    for i in range(1,n):
        a = mysqrt(i)
        b = math.sqrt(i)
        diff = abs(a-b)
        d = {i: [mysqrt(i), a, b, diff]}
        print ("{:<5} {:0.8f} {:0.8f} {:0.8f}".format(i, mysqrt(a), math.sqrt(a), diff))
# i couldnt really figure out how to solve this issues, i also just looked up how the format type text, i dont really understand how it works
test_square_root(15)
