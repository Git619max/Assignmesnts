#pattern1
for x in range(0,6):
    for y in range(0,x+1):
        print("*",end='')
    print()
print()
#pattern2
i = 6
for x in range(0,6):
    for y in range(0,i):
        print("*", end = '')
    i=i-1
    print()
print()
#pattern3
a=5
for x in range(0,6):
    for y in range(0,6):
        if(a-y>0):
            print(" ",end='')
        else:
            print("*",end='')
    a=a-1
    print()
print()
#pattern4
i=0
for x in range(0,6):
    for y in range(0,i):
        print(" ",end = '')
    for z in range(i,6):
        print("*",end='')
    i=i+1
    print()
print()