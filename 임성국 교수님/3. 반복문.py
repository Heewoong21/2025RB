
"""
a = 23
number = int(input('수를 입력하세요.'))

while number != a:  
    if a > number:
        print('틀렸습니다. 조금 더 큰 수 입니다.')
    elif a < number:
        print('틀렸습니다. 조금 더 작은 수 입니다.')
    
    number = int(input('다시 입력하세요: ')) 

print('정답입니다!')
"""
#==============================================================
"""
number = int(input('수를 입력하세요.'))

while number != 777:
  if number%3 == 0 and number%2 ==0:
    print('짝수이면서 3의 배수입니다.')
  elif number%3 == 0:
    print('3의 배수입니다.')
  elif number%2 == 0:
    print('짝수입니다.')

  number = int(input('다시 입력하세요.'))"
"""
#==============================================================
"""
import random

ans = random.randrange(1,1001)
myNumber = 0
cnt = 0

while ans != myNumber:
    myNumber = int(input('수를 입력하세요: '))
    cnt += 1
    if myNumber>ans:
      print(f'{cnt}번째 시도입니다. 틀렸습니다. 조금 더 작은 수 입니다.')
    elif myNumber < ans:
       
       print(f'{cnt}번째 시도입니다. 틀렸습니다. 조금 더 큰 수 입니다.')
    else:
       print(f'{cnt}번째 시도입니다.맞았습니다.')
"""
#===============================================================
