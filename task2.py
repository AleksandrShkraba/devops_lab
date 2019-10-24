from itertools import zip_longest
keylist = ['a', 'b', 'c', 'd', 'f']
valuelist = [1, 2, 3, 4, 5, 6, 7, 8, ]
if len(keylist) < len(valuelist):
    n = len(valuelist) - len(keylist)
    valuelist = valuelist[:len(valuelist) - n]
rezult = dict(zip_longest(keylist, valuelist))
print(rezult)
