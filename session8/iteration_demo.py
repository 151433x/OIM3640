
result=0
# for i in range(1000):
#     print(f'iteration{i}')
#     print(f'before adding {i}, current result is {result}.')
#     result+=1
#     print(f'after adding{i}, result becomes {result}.\n')
# print(result)

def oddsum():
    """calcualate the sum of all odd numbers in a range"""
    result=0
    for i in range(1000):
        print(f"interation{i}")
        if i%2==0:
            print(f"{i} is an odd number ")
            result=+1
            print(f"after adding{i}, result becomes {result}")
        print()
    return result
print(oddsum())

def sumodd2():
    for i in range(0,1001,2):
        result+=1
    return result
print(sumodd2())