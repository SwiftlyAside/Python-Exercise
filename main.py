import math
from calculator import plus, minus

def say_hello(name = "man", age = "1"):
  return f"Hello {name}, you are {age} years old."

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

print(plus(a = "10", b = 22))

print(math.ceil(1.2))
print(math.fabs(-1.2))

print(plus(1,2), minus(1,2))