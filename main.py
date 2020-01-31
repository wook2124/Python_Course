def plus(a, b):
  if type(b) is int or type(b) is float:
    return a + b
  else:
    return "Error"

a = 12
b = "asdf"

result = plus(a, b)
print(result)