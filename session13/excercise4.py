
f=open('Data/words.txt')
def wordstore_checker(f,stri):
    """will check if a word is in a dictionary and if not will input it, it will also check for the count of the word. Finally this takes a string and checks if it is in the dictionary"""
    d=dict()
    for line in f:
        word=line.strip()
        d[word]=d.get(word,0)+1
    if stri in d:
        return True
    return False
# print(wordstore_checker(f,'1234'))
a=[1,1,1,2,2,3,4,]
b=[1,2,3]
def has_duplis(list1):
    """ returns true if list has a duplicate, false if it does not """
    for i in list1:
        if list1.count(i) > 1:
            return True
    return False
# print(has_duplis(a))
# print(has_duplis(b))