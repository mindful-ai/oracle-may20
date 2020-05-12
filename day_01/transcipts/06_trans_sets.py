Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # SET
>>> 
>>> 
>>> s = 'mississippi'
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'p', 's', 'm', 'i'}
>>> 
>>> 
>>> 
>>> s1 = set('abcdefgh')
>>> s1
{'g', 'h', 'b', 'a', 'e', 'd', 'c', 'f'}
>>> s2 = {'f', 'g', 'h', 'i', 'j'}
>>> s2
{'g', 'j', 'h', 'i', 'f'}
>>> 
>>> 
>>> s1[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s1[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> 
>>> s1.add('x')
>>> s1
{'g', 'h', 'b', 'a', 'x', 'e', 'd', 'c', 'f'}
>>> s1.remove('y')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s1.remove('y')
KeyError: 'y'
>>> s1.remove('x')
>>> 
>>> 
>>> 'c' in s1
True
>>> 
>>> 
>>> s1 | s2
{'g', 'j', 'h', 'b', 'a', 'e', 'd', 'i', 'c', 'f'}
>>> s1 & s2
{'f', 'g', 'h'}
>>> s1 ^ s2
{'j', 'a', 'e', 'd', 'i', 'b', 'c'}
>>> 
>>> 
>>> s1.intersection(s2)
{'f', 'g', 'h'}
>>> s1.union(s2)
{'g', 'j', 'h', 'b', 'a', 'e', 'd', 'i', 'c', 'f'}
>>> 
