def say_hello(name = "man", age = "1"):
  return f"Hello {name}, you are {age} years old."

def plus(a, b):
  return a + b

ilan = {
  "name": "Ilan",
  "age": 27,
  "korean": True,
  "favorite": ["hardware", "coffee"]
}

print(ilan)
ilan["handsome"] = True
print(ilan)

print(int("18"))

hello = say_hello("Ilan", "22")
print(hello)

print(plus(a = 10, b = 22))