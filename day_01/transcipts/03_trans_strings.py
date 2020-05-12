Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRINGS
>>> 
>>> s = 'python'
>>> 
>>> # immutability
>>> s[0]
'p'
>>> s[2]
't'
>>> s[0] = 'j'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[0] = 'j'
TypeError: 'str' object does not support item assignment
>>> type(s)
<class 'str'>
>>> s = 'jython'
>>> s
'jython'
>>> s[0]
'j'
>>> # --------------------- Operators
>>> 
>>> s1 = 'ice'
>>> s2 = 'cream'
>>> s1 + s2
'icecream'
>>> s1 * 3
'iceiceice'
>>> 'cre' in s1 + s2
True
>>> len(s1 + s2)
8
>>> del s1
>>> del s2
>>> s1
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s1
NameError: name 's1' is not defined
>>> s2
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s2
NameError: name 's2' is not defined
>>> 
>>> # ----------------------- accesability
>>> 
>>> # s[index]
>>> # s[start_index:end_index]
>>> # s[start_index:end_index:skip_interval]
>>> 
>>> s
'jython'
>>> s = 'python'
>>> s
'python'
>>> 
>>> s[0]
'p'
>>> s[2]
't'
>>> s[5]
'n'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[-3]
'h'
>>> 
>>> s[2:5]
'tho'
>>> # 2:5 ---> 2, 3, 4 only  5  is left out
>>> # 2 inclusive, 5 not inclusive
>>> 
>>> s[0:4]
'pyth'
>>> s[:4]
'pyth'
>>> s[2:6]
'thon'
>>> s[2:]
'thon'
>>> s[:]
'python'
>>> 
>>> 
>>> s[2:5]
'tho'
>>> s[2:6]
'thon'
>>> s[2:6:2]
'to'
>>> # 2:6 ---> 2, 3, 4, 5
>>> # interval is 2  ----< 2, 4
>>> 
>>> s[::3]
'ph'
>>> 
>>> s[::-1]
'nohtyp'
>>> # [:] 0 1 2 3 4 5 6 --> python
>>> s[:]
'python'
>>> # [::2] 0 2 4 ---> pto
>>> s[::2]
'pto'
>>> 
>>> s[::3]
'ph'
>>> s[::-1]
'nohtyp'
>>> s[::-2]
'nhy'
>>> # ---------------------------- built in functions
>>> 
>>> # ----- case
>>> 
>>> p
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    p
NameError: name 'p' is not defined
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> 
>>> # -------- querying
>>> 
>>> s1 = '123'
>>> s2 = 'Ab345'
>>> s3 = ' '
>>> s4 = '(*&^%'
>>> 
>>> s
'python'
>>> s.islower()
True
>>> s.isupper()
False
>>> s.isdigit()
False
>>> s1.isdigit()
True
>>> int(s1)
123
>>> s2.isdigit()
False
>>> int(s2)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    int(s2)
ValueError: invalid literal for int() with base 10: 'Ab345'
>>> int(s2, 16)
701253
>>> s2.isalpha()
False
>>> s2.isalnum()
True
>>> s3.isspace()
True
>>> s4
'(*&^%'
>>> s4.isalnum()
False
>>> 
>>> 
>>> site = "www.oracle.com"
>>> tyep(site)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    tyep(site)
NameError: name 'tyep' is not defined
>>> type(site)
<class 'str'>
>>> site.isalnum()
False
>>> site.startswith('http')
False
>>> site.endswith('com')
True
>>> 'ora' in site
True
>>> 
>>> 
>>> # ----------------------- search
>>> 
>>> s.find('ora')
-1
>>> site.find('ora')
4
>>> site
'www.oracle.com'
>>> s
'python'
>>> s = 'mississippi'
>>> s.find('ss')
2
>>> import re
>>> re.findall('ss', s)
['ss', 'ss']
>>> for m in re.finditer('ss', s):
	print(m.group(), m.span())

	
ss (2, 4)
ss (5, 7)
>>> s[2:4]
'ss'
>>> s[5:7]
'ss'
>>> s
'mississippi'
>>> s.count('i')
4
>>> # ------------------- modifying
>>> 
>>> s = '     raj@oracle.com   '
>>> s.strip()
'raj@oracle.com'
>>> s
'     raj@oracle.com   '
>>> new = s.strip()
>>> 
>>> new
'raj@oracle.com'
>>> s
'     raj@oracle.com   '
>>> s
'     raj@oracle.com   '
>>> s
'     raj@oracle.com   '
>>> s = s.strip()
>>> s
'raj@oracle.com'
>>> s = '     raj@oracle.com   '
>>> s.lstrip()
'raj@oracle.com   '
>>> s.rstrip()
'     raj@oracle.com'
>>> 
>>> s = python
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    s = python
NameError: name 'python' is not defined
>>> s = 'python'
>>> s.rjust(20, '*')
'**************python'
>>> s.ljust(20, '*')
'python**************'
>>> s
'python'
>>> 
>>> 
>>> ip = '198-98-2-1'
>>> ip.replace('-', '.')
'198.98.2.1'
>>> ip
'198-98-2-1'
>>> 
>>> 
>>> text = "This is a test code"
>>> text.split()
['This', 'is', 'a', 'test', 'code']
>>> test.split('s')
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    test.split('s')
NameError: name 'test' is not defined
>>> text.split('s')
['Thi', ' i', ' a te', 't code']
>>> 
>>> 
>>> 
>>> L = ['This', 'is', 'a', 'test', 'code']
>>> type(L)
<class 'list'>
>>> '*'.join(L)
'This*is*a*test*code'
>>> L
['This', 'is', 'a', 'test', 'code']
>>> startext = '*'.join(L)
>>> startext
'This*is*a*test*code'
>>> 
>>> 
>>> L = ['anil', '35', 'oracle', 'India', 'USA']
>>> ','.join(L)
'anil,35,oracle,India,USA'
>>> 
