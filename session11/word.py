from ctypes.wintypes import WORD
import os
from pickle import TRUE
from traceback import format_list
from typing import Counter


# Assume words.txt is under data folder
# f = open('data/words.txt')
# line = f.readline()
# f = open('data/words.txt')

# number_of_words = 0

# for line in f:
#     word = line.strip()
#     number_of_words += 1
# print(number_of_words)

# def find_long_words():
#     """
#     prints only the words with more than 20 characters
#     """
#     f = open('data/words.txt')  # Assume words.txt is under data folder
#     for line in f:
#         word = line.strip()
#         if len(word) > 20:
#             print(word, len(word))
# # find_long_words()


# def has_no_e(word):
#     """
#     returns True if the given word doesn’t have the letter "e" in it
#     """
#     for letter in word:
#         if letter =='e':
#             return False
#     return True
# # print(has_no_e('Babson')) 
# # print(has_no_e('College'))
# # print(has_no_e('EA sports'))


# def find_words_no_e():
#     Counter=0
#     noecounter=0
#     f = open('Data/words.txt')
#     for line in f:
#         Counter += 1
#         word = line.strip()
#         if has_no_e(word) == True:
#             noecounter+=1
#             print(word)
#     print('Percentage of words with no e', noecounter/Counter)
# find_words_no_e()


# def avoids():
#     """
#     returns True if the given word does not use any of the forbidden letters.
#     """
#     word=input("please put in the word you want to check ")
#     forlist=input("please put in a list of letters that you don't want to to be in the words. ")
#     for letter in word:
#         if letter in forlist:
#             return False
#     return True

def uses_only(available):
    """
     a string of letters, and that returns the number of words in the list that only have these letters."
    """
    f = open('data/words.txt')
    line = f.readline()
    line=line.strip()
    yescounter=0
    for line in f:
        for letter in line: 
            if letter in available:
                yescounter+=1
                print(line) 
    return yescounter
print(uses_only("planets"))
                

#         Counter += 1
#         word = line.strip()
#         if has_no_e(word) == True:
#             noecounter+=1
#             print(word)




# # print(uses_only('Babson', 'aBbsonxyz'))
# # print(uses_only('college', 'aBbsonxyz'))


# def find_words_only_use_planet():
#     """"""
#     pass


# # print('Number of words that use only letters from "planets" is', find_words_only_use_planet())


# def uses_all(word, required):
#     """
#     takes a word and a string of required letters, and that returns True if
#     the word uses all the required letters at least once.
#     """
#     pass


# # please write test cases


# def find_words_using_all_vowels():
#     """
#     return the number of the words that use all the vowel letters
#     """
#     pass


# # print('The number of words that use all the vowels:', find_words_using_all_vowels())


# def is_abecedarian(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     pass


# # print(is_abecedarian('abs'))
# # print(is_abecedarian('college'))


# def find_abecedarian_words():
#     """
#     returns the number of abecedarian words
#     """
#     pass


# # print(find_abecedarian_words())


# def is_abecedarian_using_recursion(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     pass


# # print(is_abecedarian_using_recursion('abcdef'))


# def is_abecedarian_using_while(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     pass

# print(is_abecedarian_using_while('abcdef')