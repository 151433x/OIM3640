
# def histogram(s):
#     d=dict()
#     for c in s:
#         if c not in d:
#             d[c]=1
#         else:
#             d[c]+=1
#     return d
# # # print(histogram('bookkeeper'))

# # names=['john','paul','george']
# # scores=[95,75,85]

# # grades= dict()
# # print(grades)

# # grades['john']=90
# # print(grades)

# # grades={'john':90,'paul':75,'george':85}
# # print(grades)

# # print(grades['paul'])
# # # print(grades['ringo'])

# # print(len(grades))
# # 'paul' in grades

# # 90 in grades.values()

# # #looping and dictionaries
# # def print_hist(h):
# #     for c in h:
# #         print(c,h[c])
# # h=histogram('Massachusetts')
# # print(print_hist(h))

# # for key in sorted(h):
# #     print(key,h[key])

# # reverse lookup

# # def reverse_lookup(d,v):
# #     for k in d:
# #         if d[k]==v:
# #             return k
# #     raise LookupError()
# # h=histogram('Massachusetts')
# # key=reverse_lookup(h,2)
# # print(key)

# # dictionaries and lists inversion


# def invert_dict(d):
#     inverse=dict()
#     for key in d:
#         val=d[key]
#         if val not in inverse:
#             inverse[val]=[key]
#         else:
#             inverse[val].append(key)
#     return inverse
# hist=histogram('parrot')
# print(hist)

# inverse=invert_dict(hist)
# print(inverse)

# t=[1,2,3]
# d=dict()
# d[t]='oops' # will cause error as lists cannot be keys in dictionaries

# #memos
# known= {0:0, 1:1}
# def fibonacci(n):
#     if n in known:
#         return known[n]
#     res= fibonacci(n-1)+ fibonacci(n-2)
#     known[n]=res
#     return res
# for i in range(10):
#     print(fibonacci(i),end=",")