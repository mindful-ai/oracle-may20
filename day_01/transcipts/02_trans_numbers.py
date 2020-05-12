Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # NUMBERS
>>> 
>>> a = 10
>>> b = 1.45
>>> c = -56
>>> d = 3/5
>>> 
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'int'>
>>> type(d)
<class 'float'>
>>> 
>>> 
>>> a
10
>>> b
1.45
>>> c
-56
>>> d
0.6
>>> 
>>> print(a)
10
>>> pritn(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    pritn(b)
NameError: name 'pritn' is not defined
>>> print(b)
1.45
>>> print(c)
-56
>>> print(d)
0.6
>>> 
>>> 
>>> # Operations
>>> 
>>> # Arithmetic Operator
>>> 
>>> a = 5
>>> b = 3
>>> a + b
8
>>> a - b
2
>>> a * b
15
>>> a / b
1.6666666666666667
>>> a % b
2
>>> a // b
1
>>> 7 % 3
1
>>> 7 // 3
2
>>> 7/3
2.3333333333333335
>>> 
>>> a ** 2
25
>>> 
>>> # Relational operations
>>> 
>>> a > b # is a greater than b?
True
>>> a < b
False
>>> a == b
False
>>> a == b + 3
False
>>> a
5
>>> b
3
>>> a == b + 2
True
>>> a != 5
False
>>> a >= 5
True
>>> a <= 5
True
>>> 
>>> 2 < a < 10  # is 2 < a and a < 10?
True
>>> 
>>> 
>>> # Logical operators
>>> 
>>> # and or not
>>> # Logical values: True False  ---> Boolean values
>>> 
>>> 
>>> a == b ** 2 or a == b + 2
True
>>> a == b ** 2 and a == b + 2
False
>>> not (a == b ** 2 and a == b + 2)
True
>>> 
>>> 
>>> # ---------------------------- IN BUILT FUNTIONS
>>> 
>>> s = '123'
>>> type(s)
<class 'str'>
>>> s + a
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s + a
TypeError: can only concatenate str (not "int") to str
>>> int(s) + a
128
>>> s + str(a)
'1235'
>>> s
'123'
>>> bin(s)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    bin(s)
TypeError: 'str' object cannot be interpreted as an integer
>>> bin(int(s))
'0b1111011'
>>> '0b1111011'
'0b1111011'
>>> a = 100
>>> hex(a)
'0x64'
>>> oct(a)
'0o144'
>>> bin(a)
'0b1100100'
>>> 
>>> s = '1101'
>>> int(s)
1101
>>> int(s, 2)
13
>>> 
>>> 
>>> # ---------------------------- MOdules
>>> 
>>> s = '10A'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '10A'
>>> int(s, 16)
266
>>> hex(266)
'0x10a'
>>> 
>>> 
>>> s = '1101'
>>> int(s) + 9
1110
>>> int(s) + 9
1110
>>> int(s, 2) + 9
22
>>> s = '10A'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '10A'
>>> int(s, 16)
266
>>> int(s, 8)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    int(s, 8)
ValueError: invalid literal for int() with base 8: '10A'
>>> int(s, 2)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    int(s, 2)
ValueError: invalid literal for int() with base 2: '10A'
>>> s = "12A^"
>>> # ------------------------
>>> 
>>> import math
>>> 
>>> math.sqrt(100)
10.0
>>> sqrt(100)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    sqrt(100)
NameError: name 'sqrt' is not defined
>>> math.gcd(18, 98)
2
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(math.radians(90))
1.0
>>> math.sin(90 * math.pi/180)
1.0
>>> 
