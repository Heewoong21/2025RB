name = 'Baram'

if name.startswith('Bar'):
    print('Yes, the string starts with "Bar"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('ara') != -1:
    print('Yes, it contains the string "ara"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

#파이썬의 모든 문자열은 str 클래스의 객체