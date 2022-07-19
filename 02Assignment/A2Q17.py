L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print("Original list =",L)
L = [t for t in L if t]
print(L)