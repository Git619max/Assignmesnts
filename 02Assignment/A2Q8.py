def check_prime(number):
    counter = 0
    for x in range(1,number+1):
        if(number%x==0):
            counter = counter + 1
    if(counter>2):
        print("not prime")
    else:
        print("prime")
check_prime(19)
        