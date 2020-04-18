def count_vowels(txt):
    if txt == '': return 0
    if txt[0] in [a, e, i, o, u ]:
        p=1
    else:
        p=0
    return p + length(txt[1:])

def filter_list(lst):
    if lst == []: return 0
    if type(lst[0])== str: lst.remove(lst[0])
    filter_list(lst[1:])
    return lst

filter_list([1, 2, "a", "b"])
max()

d= {}
d.update({})



def combinations(*args):
    l = list(args)
    temp = 1
    for i in l:
        if i is 0: next
    	temp*=i
    return temp
