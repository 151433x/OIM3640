def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d
# print(histogram('bookkeeper'))


def historgram2(s):
    d=dict()
    for c in s:
        d[c]=d.get(c,0)+1
    return d
print(historgram2('bookeeper'))
