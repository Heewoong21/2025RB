"""
shoplist = ['apple', 'mango','carrot', 'banana']

print('I have', len(shoplist), 'items to purchase')
print('These itmes are: ', end=' ')

for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')

shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I willl sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]

del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)"
"""
#====================================================
"""
#메소드 확인
a=[0,1]
print(dir(a))
"""

#range(10)...0~9
"""
for i in range(10):
  print(i,end=' ')

print(range(10))
print(list(range(10)))"
"""

#====================================================
#친구들의 리스트 생성하기
"""
friend_list=[]
for i in range(5):
   friend_list.append(input('친구들의 이름을 입력하시오.'))

print(friend_list)
"""
#====================================================
#튜플
"""
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo='monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))

print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', \
      len(new_zoo)-1+len(new_zoo[2]))
"""
#====================================================
#딕셔너리
"""
#'ab' is short for 'a'ddress 'b'ook
ab = {'Baram': 'ludenscode@gmail.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }
print("Baram's address is ", ab['Baram'])

#Deleting a key-value pair
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
  print('Contact {} at {}'.format(name, address))

#Adding a key-value pair
ab['Gildong'] = 'gildong@ueldo.org'

if 'Gildong' in ab:
  print("\n Gildong's address is", ab['Gildong'])

"""
#====================================================
"""
ab = {'Baram': 'ludenscode@gmail.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }
for name in ab:
    print(name)

for name in ab:
    print(name, ab[name])

for name, address in ab.items():
    print(name, address)
"""
#====================================================
"""
#for comprehence
temperatures = [2, 5, 8, 10, 50, 80, 12, 52, 99]

t_20 = []

for temp in temperatures:
  if temp>= 20:
    t_20.append(temp)

print(t_20)
"""
#====================================================
"""
#list comprehence
temperatures = [2, 5, 8, 10, 50, 80, 12, 52, 99]

t20 =[i for i in temperatures if i>=20]

print(t20)
"""
#====================================================