def say_hello(name, age, where_from, fav_food):
  return f"Hello {name}, you are {age} years old? And you are from {where_from} right? So {fav_food} is your favorite food??"

hello = say_hello(age="27", fav_food="참치마요", where_from="Korea", name="Wook")
print(hello)