def my_abs(x):
    if isinstance(x, int | float):
        return (x**2)**.5
    return "this is the wrong type of data. PLease input a integer or float value"


print(my_abs(3))
print(my_abs(-12))


def quadratic(a, b, c):
    # quadratic formula in [-b+-(sqrt(b^2-4ac))]/2a
    root1 = (-b-((b**2)*(-4*a*c))**.5)/(2*a)  # calculate negative root
    root2 = (-b+((b**2)*(-4*a*c))**.5)/(2*a)  # calculate positive root
    return root1, root2


print(quadratic(1, 1, -5))

2**38