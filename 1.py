Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = ' Narupon '
print(name)
 Narupon 
type(namr)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(namr)
NameError: name 'namr' is not defined. Did you mean: 'name'?
type(name)
<class 'str'>
name.lower()
' narupon '
name.upper()
' NARUPON '
friend = ' aun '
print('สวัสดีอุนสบายดีไหม?')
สวัสดีอุนสบายดีไหม?
print('สวัสดี'+friend+'สบายดีไหม?')
สวัสดี aun สบายดีไหม?
money = 10
print('อุนยืมเงิน 10 บาท')
อุนยืมเงิน 10 บาท
print(friend) + print('ยืมเงิน') + print(money) + print('บาท')
 aun 
ยืมเงิน
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(friend) + print('ยืมเงิน') + print(money) + print('บาท')
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
type(money)
<class 'int'>
print(friend + 'ยืมเงิน' + str(money) + 'บาท')
 aun ยืมเงิน10บาท
print('{}ยืมเงิน{}บาท'.format(friend,money))
 aun ยืมเงิน10บาท
print(f'{friend}ยืมเงิน {money} บาท')
 aun ยืมเงิน 10 บาท
money2 = 12345678
print(money + money2)
12345688
print(f'{money:,}')
10
print(f'{money2:,}')
12,345,678
>>> print(f'{money2:,.2f}')
12,345,678.00
>>> improt math
SyntaxError: incomplete input
>>> import math
>>> print(pi)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(pi)
NameError: name 'pi' is not defined
>>> print('pi)
...       
SyntaxError: incomplete input
>>> math.pi
...       
3.141592653589793
>>> math.pi * (5 ** 2)
...       
78.53981633974483
>>> from datetime import datetime
...       
>>> datetime.now()
...       
datetime.datetime(2023, 2, 10, 7, 13, 16, 604552)
>>> datetime.now() .strftime(%Y%m%d %H:%M:%S)
...       
SyntaxError: invalid syntax
>>> datetime.now() .strftime('%Y%m%d %H:%M:%S')
...       
'20230210 07:14:18'
>>> import random
>>> random.randint(1,7)
1
>>> random.randint(1,99)
22
>>> store = ['ป้าส้ม','ป้าเล็ก','ลุงดำ']
>>> random.choice(store)
'ป้าส้ม'
>>> random.choice(store)
'ป้าส้ม'
>>> random.choice(store)
'ป้าเล็ก'
>>> random.choice(store)
'ป้าเล็ก'
>>> random.choice(store)
'ลุงดำ'
>>> random.choice(store)
'ป้าเล็ก'
