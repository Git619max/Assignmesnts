def average_tuple(tuple1):
    result = [sum(x) / len(x) for x in zip(*tuple1)]
    return result

tuple1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print ("Original Tuple: ")
print(tuple1)
print("Average :",average_tuple(tuple1))