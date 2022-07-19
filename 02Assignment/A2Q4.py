from calendar import c


def check_arm(number):
    x = number
    ans = 0
    while(x>0):
        temp = x%10
        ans = ans + temp**3
        x=x//10
    if(ans==number):
        print("Armstrong No.")
    else:
        print("Not armstrong no.")
check_arm(153)
    