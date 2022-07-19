def average(list1):
    avg = 0
    for x in range(0,len(list1)):
        avg = avg+list1[x]
    return avg/len(list1)
glist = [10,20,30,40]
print(max(glist))
print(min(glist))
print(average(glist))