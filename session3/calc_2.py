# the volume of the sphere with radius r is
# (4/3)pir^3
# what is the volume of a sphere with radius of 5?
from time import time


pi = 3.1415
radius = 5
v = (4/3)*(pi)*(radius**3)
print(v)
# the outcome is 523.58 which is the volume of the sphere

# 2.suppose the cover price of the book is $24.95 but the bookstores get a 40% discount. Shipping costs 3$ for the first copy and 75 cents for each additional copy. What is total wholesale cost of 60 copies?

n = 60  # number of books ordered
p = 24.95
scost = .75
cost_for_bookstore = 24.95*.6  # cost is 9.98
total_wholesale_cost = (cost_for_bookstore*n)+3+(scost*n-1)  # 945.19
print(total_wholesale_cost)

# 3. If leave my house at 6:52am and run 1 mile at an easy pace(8:15 per mile), then 3 miles at tempo(7:12 per mile) and 1 mile at a easy pace again, what time do I get home for breakfest?

starting_time_minutes = 6*60+52  # 412 minutes
starting_time_seconds = starting_time_minutes*60
print(starting_time_seconds)  # 24720

tempo_seconds = 7*60+12
tempo_total = tempo_seconds*3
print(tempo_total)  # 1296
easy_seconds = 8*60+15
easy_total = easy_seconds*2
print(easy_total)  # 998
total_seconds = tempo_total+starting_time_seconds+easy_total
print(total_seconds)
time_minutes = total_seconds/60
print(time_minutes)  # 450 minutes
time_hours = time_minutes/60
print(time_hours)
print(time_minutes % 60)  # 30.1 mintures for reminder or 7:30am

# If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as xx.x%. Keep one figure after decimal point.

gpa_before = 82
gpa_after = 89

percentag1 = (gpa_after-gpa_before)/gpa_before*100
print(percentag1)
print(f'the percentage is {percentag1:.1f}%')  # 8.5%
