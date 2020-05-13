Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # For loop
>>> 
>>> for ch in "python":    # for ever ch in the string "python"
	print("Hello World!")

	
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
>>> for ch in "python":    # for ever ch in the string "python"
	print("Hello World! ", ch)

	
Hello World!  p
Hello World!  y
Hello World!  t
Hello World!  h
Hello World!  o
Hello World!  n
>>> 
>>> for item in ['red', 'green', 'blue', 'yellow']:
	print(item.upper())

	
RED
GREEN
BLUE
YELLOW
>>> for item in ('red', 'green', 'blue', 'yellow'):
	print(item.upper())

	
RED
GREEN
BLUE
YELLOW
>>> 
>>> s = 'mississippi'
>>> for elem in set(s):
	print(elem)

	
i
m
p
s
>>> 
>>> D = {'name':'Anil', 'age':35, 'country':'Israel', 'company': 'oracle'}
>>> for item in D:
	print(item)

	
name
age
country
company
>>> for item in D.keys():
	print(item)

	
name
age
country
company
>>> for item in D.values():
	print(item)

	
Anil
35
Israel
oracle
>>> 
>>> for item in D.items():
	print(item)

	
('name', 'Anil')
('age', 35)
('country', 'Israel')
('company', 'oracle')
>>> 
>>> key, value = ('name', 'Anil')
>>> key
'name'
>>> value
'Anil'
>>> for k, v in D.items():
	print(k, ' -----> ', v)

	
name  ----->  Anil
age  ----->  35
country  ----->  Israel
company  ----->  oracle
>>> 
>>> 
>>> 
>>> # ----------------------- Sunita
>>> 
>>> D=( 'name': 'Anil', 'age':'35', 'country': 'Israel', 'company':'Oracle')
SyntaxError: invalid syntax
>>> D1={ 'name': 'Anil', 'age':'35', 'country': 'Israel', 'company':'Oracle' }
>>> D1.items()
dict_items([('name', 'Anil'), ('age', '35'), ('country', 'Israel'), ('company', 'Oracle')])
>>> 
>>> 
>>> for item in D.items():
	print(item)

	
('name', 'Anil')
('age', 35)
('country', 'Israel')
('company', 'oracle')
>>> 
>>> 
>>> a, b = ('country', 'Israel')
>>> a
'country'
>>> b
'Israel'
>>> 
>>> 
>>> # ---------------------------- Megan
>>> 
>>> for a, b in D1.items():
	print(a, b)

	
name Anil
age 35
country Israel
company Oracle
>>> 
>>> 
>>> # --------------------------------------------------
>>> 
>>> 
>>> n = 1234
>>> for x in n:
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    for x in n:
TypeError: 'int' object is not iterable
>>> for x in str(n):
	print(x)

	
1
2
3
4
>>> sumn = 0
>>> for x in str(n):
	sumn += x

	
Traceback (most recent call last):
  File "<pyshell#78>", line 2, in <module>
    sumn += x
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
>>> for x in str(n):
	sumn += int(x)

	
>>> print(sumn)
10
>>> 
>>> # ---------------------
>>> # Print the multiplication table
>>> 
>>> # 5 X 1 = 5
>>> 
>>> for c in "python":
	print("5 X 1 = 5")

	
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
5 X 1 = 5
>>> 
>>> N = [1, 2, 3, 4, 5]
>>> for c in N:
	print('5' + ' X ' + str(c) + ' = ' + str(5 * c))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20, 30))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(1, 100, 3))
[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97]
>>> 
>>> 
>>> for c in range(10):
	print('5' + ' X ' + str(c) + ' = ' + str(5 * c))

	
5 X 0 = 0
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
>>> for c in range(1, 11):
	print('5' + ' X ' + str(c) + ' = ' + str(5 * c))

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> 
>>> 
>>> n = 1
>>> while n <= 10:
	print('5' + ' X ' + str(n) + ' = ' + str(5 * n))
	n += 1

	
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
>>> 
>>> 
>>> # ---------------------- Loop control statements
>>> 
>>> # break - breaks the loop abruptly
>>> 
>>> for c in range(1, 11):
	if(c % 3 == 0):
		break
	print('5' + ' X ' + str(c) + ' = ' + str(5 * c))

	
5 X 1 = 5
5 X 2 = 10
>>> 
>>> 
>>> # continue - skips the iteration
>>> 
>>> for c in range(1, 11):
	if(c % 3 == 0):
		continue
	print('5' + ' X ' + str(c) + ' = ' + str(5 * c))

	
5 X 1 = 5
5 X 2 = 10
5 X 4 = 20
5 X 5 = 25
5 X 7 = 35
5 X 8 = 40
5 X 10 = 50
>>> 
>>> 
>>> 
>>> # ---------------------------------------------
>>> 
>>> 
>>> sumn = 0
>>> for x in str(n):
umn += int(x)    print(sumn)
SyntaxError: expected an indented block
>>> for x in str(n):
	sumn += int(x)    print(sumn)
	
SyntaxError: unindent does not match any outer indentation level
>>> for x in str(n):
	sumn += int(x)
	print(sumn)

	
1
2
>>> n = 1234
>>> for x in str(n):
	sumn += int(x)
	print(sumn)

	
3
5
8
12
>>> sumn = 0
>>> for x in str(n):
	sumn += int(x)
	print(sumn)

	
1
3
6
10
>>> sumn = 0
>>> for x in str(n):
	sumn += int(x)
	
SyntaxError: multiple statements found while compiling a single statement
>>> sumn = 0
>>> for x in str(n):
	sumn += int(x)

	
>>> print(sumn)
10
>>> 
>>> # -------------------- Sunita
