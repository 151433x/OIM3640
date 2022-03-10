import pprint as pprint
def wordlist(path):
    f= open(path)
    d=list()
    for line in f:
        word=line.strip()
        d.append(word)
    return d
def keylist(d):
    e=list()
    for i in d:
        e.append(''.join(sorted(i)))
    return e
def anagrams(wordlist,keylist):
    d={}
    finald={}
    for i in range(len(wordlist)):
        key=keylist[i]
        value=wordlist[i]
        d[key]=d.get(value,[])
        d[key].append(value)
    for key in d:
        value=d[key]
        if len(value)>3:
            finald[key]=value
    return sorted(list(finald.values()),key=len,reverse=True)
           

a=wordlist('data/words.txt')
pprint.pprint(anagrams(a,keylist(a)))    

# pprint.pprint(a)
# pprint.pprint(keylist(a))

