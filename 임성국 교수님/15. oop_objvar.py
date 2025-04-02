class Robot:
  """Represents a robot, with a name."""
  # A class variable, counting the number of robots
  population = 0 #클래스 변수

  def __init__(self,name):
    """Initializes the data."""
    self.name = name #객체 변수
    print("(Initializing {})".format(self.name)) #보통 사용X
    # When this person is created, the robot
    # adds to the population
    Robot.population += 1

  def die(self): #객체 메서드
    """I am dying"""
    print("{} is being destroyed!".format(self.name))

    Robot.population -= 1

    if Robot.population == 0:
      print("{} was the last one.".format(self.name))
    else:
      print("There are still {:d} robots working.".format(Robot.population))

  def say_hi(self): #객체 메서드
    """Greeting by the robot. Yeah they can do that."""
    print("Greetings, my masters call me {}".format(self.name))
  
  #클래스 메서드 만드는 방법
  @classmethod #예약어 데코레이터
  def how_many(cls): #매개변수 이름 cls 사용
    """Prints the current population."""
    print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished work. So let's destrpoy them.")

droid1.die()
droid2.die() 
Robot.how_many()