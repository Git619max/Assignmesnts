def s1(str):
  if len(str)<2:
    return" "

  return str[0:2]+str[-2:]

print(s1("hello"))
print(s1("he"))  
print(s1("h"))