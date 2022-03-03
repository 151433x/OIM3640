# t = [[1, 2], [3], [4, 5, 6]]
# def nested_sum(t):
#     """Computes the total of all numbers in a list of lists."""
#     # t: list of list of numbers
#     # returns: number
#     # Expected output:
#     total=0
#     for i in t:
#         total +=sum(i)
#     return total
# print(nested_sum(t))




# t = [1, 2, 3]
# def cumsum(t):
#     """Computes the cumulative sum of the numbers in t."""
#     # t: list of numbers
#     # returns: list of numbers
#     # Expected output: [1, 3, 6]
#     t1=t[0]
#     t2=t[1]+t1
#     t3=t[2]+t2
#     return t1,t2,t3
#  print(cumsum(t))
# t = [1, 2, 3, 4]
# def middle(t):
#     """Returns all but the first and last elements of t."""
#     # t: list
#     # returns: new list
#     # Expected output:
#     # >>> middle(t)
#     # [2, 3]
#     d=t[1:3]
#     return d 
# print(middle(t))

# t = [1, 2, 3, 4]
# def chop(t):
#     """Removes the first and last elements of t."""
#     # t: list
#     # returns: None
#     # Expected output:
#     # >>> chop(t)
#     # >>> t
#     # [2, 3]
#     del t[0]
#     del t[-1]
#     return t
# print(chop(t))

# t=[1,2,2]
# a=['b','a']
# def is_sorted(t):
#     """Checks whether a list is sorted."""
#     # t: list
#     # returns: boolean
#     # Expected output:
#     # >>> is_sorted([1, 2, 2])
#     # True
#     # >>> is_sorted(['b', 'a'])
#     # False
#     if t !=t.sort():
#         return False
#     return True
# print(is_sorted(a)) #not sure why it doesnt work
# print(is_sorted(t))

# def is_anagram(word1, word2):
#     """Checks whether two words are anagrams
#     Two words are anagrams if you can rearrange the letters from one to
#     spell the other."""
#     # word1: string or list
#     # word2: string or list
#     # returns: boolean
#     # Expected output:
#     # >>> is_anagram('stop', 'pots')
#     # True
#     # >>> is_anagram('different', 'letters')
#     # False
#     # >>> is_anagram([1, 2, 2], [2, 1, 2])
#     # True
#     for i in word1:
#         if i not in word2:
#             return False
#     return True
# print(is_anagram('stop','pots'))
# print(is_anagram('different','letters'))
# print(is_anagram([1,2,2],[2,1,2]))

# def has_duplicates(s):
#     """Returns True if any element appears more than once in a sequence.
#     s: string or list
#     returns: bool
#     output:
#     >>> print(has_duplicates('cba'))
#     False
#     >>> print(has_duplicates('abba'))
#     True
#     """
#     for i in s:
#         if s.count(i) >1:
#             return True
#     return False
# print(has_duplicates('cba'))
# print(has_duplicates('abba'))

# def has_adjacent_duplicates(s):
#     """Returns True if there are two same adjacent elements.
#     s: string or list
#     returns: bool
#     output:
#     >>> print(has_adjacent_duplicates('cba'))
#     False
#     >>> print(has_adjacent_duplicates('abca'))
#     Flase
#     >>> print(has_adjacent_duplicates('abbc'))
#     True
#     """
#     for i in range(len(s)):
#         if i != 0:
#             if s[i] == s[i-1]:
#                 return True
#     return False
# t=['c','b','a']
# d=['a','b','c','a']
# e=['a','b','b','c']
# print(has_adjacent_duplicates(t))
# print(has_adjacent_duplicates(d))
# print(has_adjacent_duplicates(e))


# def main():
#     t = [[1, 2], [3], [4, 5, 6]]
#     # print(nested_sum(t))

#     # t = [1, 2, 3]
#     # print(cumsum(t))

#     # t = [1, 2, 3, 4]
#     # print(middle(t))
#     # chop(t)
#     # print(t)

#     # print(is_sorted([1, 2, 2]))
#     # print(is_sorted(['b', 'a']))

#     # print(is_anagram('stop', 'pots'))
#     # print(is_anagram('different', 'letters'))
#     # print(is_anagram([1, 2, 2], [2, 1, 2]))

#     # print(has_duplicates('cba'))
#     # print(has_duplicates('abba'))


# if __name__ == "__main__":
#     main()