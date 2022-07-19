def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

roll_no = ["S001", "S002", "S003", "S004"] 
s_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
marks = [85, 98, 89, 92]
print("\nNested dictionary:")
print(nested_dictionary(roll_no, s_name, marks))