"""
class Person:
  pass

p = Person()
print(p)
"""
#---------------------------------------
"""
class Person:
  def say_hi(self):
    print('Hello, how are you?')

p = Person()
p.say_hi()

#print(p)
"""
#----------------------------------------
#init 메서드
class Person:
  def __init__(self, name):
    self.name = name

  def say_hi(self):
    print('Hello, my name is', self.name)

p = Person('Baram')
p.say_hi()