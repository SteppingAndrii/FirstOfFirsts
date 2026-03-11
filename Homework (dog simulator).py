class Dog:
  def __init__(self, height=50, age=1, happiness=50):
      self.height = height
      self.age = age
      self.happiness = happiness

  def grow(self, height=1):
      self.height += height

  def grow_age(self, age=1):
      self.age += age

  def play(self, happiness=1):
      self.happiness += happiness


you = Dog()

you.grow(height=20)

while True:
  print(f"Your stats:\nAge - {you.age}\nHeight - {you.height}\nHappiness - {you.happiness}%")

  action = input("You're a dog , what do you want to do? (play/grow/age) ")

  if action == "play":
    you.play(10)
  elif action == "grow":
    you.grow(2)
  elif action == "age":
    you.grow_age(1)
  else:
    print("Sorry, cant do that")

  if you.happiness >= 100:
    you.happiness = 100
