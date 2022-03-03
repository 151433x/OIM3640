# What is the index of 'Apple'? 'Lisa'? 'On Rail'?

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', ['Ruby', 'On Rail'], 'PHP'],
#     ['Adam', 'Bart', 'Lisa']    
# ]
# print(L[0][0]) # since this is a list of lists, we choose the list we want to pick first, so this would be the first list, python starts at 0 so it would be list 0 and the first element of the list which is also 0
# print(L[2][2]) # 3rd list so 2 and 3rd element so also 2
# print(L[1][2][1]) # this is a list in a list in a list, so it would be 2nd list so 1, 3rd element which is 2 and 2 element in that list whichi is 1

# numbers = [2, 0, 1, 6, 9]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
    
# print(numbers)
# # Q. What is the length of the following list?

# my_list = ['spam', 1, ['New England Patriots', 
#                        'Buffalo Bills', 'Miami Dolphins', 
#                        'New York Giants'], 
#            [1, 2, 3]]
# print(len(my_list)) # the length of this list is 4 beacuase there are 4 elements in the list, each element is treated the same, a list or not is the same when counting length

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
# [0] * 4

# ['Tom Brady', 'Bill Belichick'] * 3 # repeats the list x amount of times, x=3

t = ['a', 'b', 'c', 'd', 'e', 'f']
# Q. How do we get ['b', 'c']? ['a', 'b', 'c', 'd']? ['d', 'e', 'f'] ? The entire list?

t = ['a', 'b', 'c', 'd', 'e', 'f']
reallist=(t[1:3],t[0:4],t[-3:])

# t[1:3] = ['x', 'y']
print(reallist)

#this was pretty helpful Link: https://towardsdatascience.com/the-basics-of-indexing-and-slicing-python-lists-2d12c90a94cf
