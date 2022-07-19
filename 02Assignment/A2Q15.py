set1 = {10,20,30,40,50}
set2 = {10,30,40}
print("Set1 =",set1)
print("Set2 =",set2)
if(set2.issubset(set1)):
    print("Set2 is subset of Set1")
else:
    print("Set2 is not subset of Set1")