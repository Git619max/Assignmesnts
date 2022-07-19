def rev_list(list1):
    list2= []
    for x in list1:
        list2.insert(0,x)
    return list2
glist = [10, 20, 30]
print(rev_list(glist))