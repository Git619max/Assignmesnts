def factorial(x):
    ans = 1
    if(x==0 or x==1):
        return 1
    for i in range(1,x+1):
        ans = ans*i
    return ans
print(factorial(5))