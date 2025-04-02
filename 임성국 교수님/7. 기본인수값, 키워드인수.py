#기본인수값
"""
def say(message, times = 1):
  print(message, times)

say('Hello')
say('World', 5)
"""
#=====================================================
#키워드 인수 장점
def func(a, b = 5, c =10):
  print('a is', a, 'and b is ', b, 'and c is', c)

func(3,7)
func(25,c = 24)
func(c = 5, a= 100)