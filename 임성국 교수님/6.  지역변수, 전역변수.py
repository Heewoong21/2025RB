#지역변수 사용시 값의 변화
"""
x = 50
def func(x):
  print('x의 값은', x)
  x = 2
  print('지역변수 x의 값은', x)

func(x)
print('x는 여전히 ', x)
"""
#============================================
#전역변수 사용 예
"""
x = 50
def func():
  global x
  print('x is ', x)
  x = 2
  print('Changed global x to ', x)

func()
print('Value of x is ', x)
"""