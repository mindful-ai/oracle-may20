Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Tupleas
>>> # TUPLES
>>> 
>>> 
>>> T = ('red', 'green', 'blue')
>>> T[0]
'red'
>>> T[1:2]
('green',)
>>> T[::-1]
('blue', 'green', 'red')
>>> 
>>> 
>>> T[0] = 'orange'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    T[0] = 'orange'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> sorted(T)
['blue', 'green', 'red']
>>> T
('red', 'green', 'blue')
>>> list(reversed(T))
['blue', 'green', 'red']
>>> T
('red', 'green', 'blue')
>>> 
>>> 
>>> 'red' in T
True
>>> T.index('red')
0
>>> T.count('red')
1
>>> 
>>> 
>>> T
('red', 'green', 'blue')
>>> T + ('white', 'black')
('red', 'green', 'blue', 'white', 'black')
>>> T
('red', 'green', 'blue')
>>> T * 2
('red', 'green', 'blue', 'red', 'green', 'blue')
>>> len(T + T1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    len(T + T1)
NameError: name 'T1' is not defined
>>> len(T + T)
6
>>> del T[0]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    del T[0]
TypeError: 'tuple' object doesn't support item deletion
>>> del T
>>> T
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    T
NameError: name 'T' is not defined
>>> 
>>> 
>>> 
>>> T = 'red', 'green', 'blue', 'yellow'
>>> T
('red', 'green', 'blue', 'yellow')
>>> type(T)
<class 'tuple'>
>>> 
>>> r,g,b,y = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> y
'yellow'
>>> 
>>> T = 'red', 'green', 'blue', 'yellow', 'orange'
>>> r,g,b,y = T
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    r,g,b,y = T
ValueError: too many values to unpack (expected 4)
>>> r,g,b,*y = T
>>> r
'red'
>>> g
'green'
>>> b
'blue'
>>> y
['yellow', 'orange']
>>> 
>>> 
>>> r,g,b,y,o,k = T
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    r,g,b,y,o,k = T
ValueError: not enough values to unpack (expected 6, got 5)
>>> r,g,b,y,o,k = T + ('',)
>>> k
''
>>> # ---------------------------------
>>> 
>>> T
('red', 'green', 'blue', 'yellow', 'orange')
>>> T.insert(1, 'pink')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    T.insert(1, 'pink')
AttributeError: 'tuple' object has no attribute 'insert'
>>> L = list(T)
>>> L
['red', 'green', 'blue', 'yellow', 'orange']
>>> L.insert(1, 'pink')
>>> L
['red', 'pink', 'green', 'blue', 'yellow', 'orange']
>>> T = tuple(L)
>>> T
('red', 'pink', 'green', 'blue', 'yellow', 'orange')
>>> 
