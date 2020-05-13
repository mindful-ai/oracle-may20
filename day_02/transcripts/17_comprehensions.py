Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # COMPREHENSIONS
>>> 
>>> # list, tuple, set, dictionary comprehensions
>>> # [] () {} {}
>>> # It's a technique to process collections in a systematic and
>>> # concise manner
>>> 
>>> L = []
>>> for n in range(1, 1000):
	if(n % 5 == 0 and n % 7 == 0):
		L.append(n)

		
>>> L
[35, 70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455, 490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910, 945, 980]
>>> 
>>> 
>>> LC = [x for x in range(1, 1000) if x % 5 == 0 and x % 7 == 0]
>>> LC
[35, 70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455, 490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910, 945, 980]
>>> 
>>> 
>>> # Formula: [<expr> <loop> <condition>]
>>> # Formula: [<expr> <loop> <condition>]
>>> 
>>> 
>>> 
>>> L = list(range(100))
>>> L = list(range(10))
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> LC = [x**2 for x in L]
>>> LC
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> LC = [x**2 for x in L if x % 2 == 0]
>>> LC
[0, 4, 16, 36, 64]
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> LC = [ (x, x**2, x**3) for x in L ]
>>> LC
[(0, 0, 0), (1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729)]
>>> L = ['apples', 'coconut', 'giraffe', 'lion']
>>> D = {key:count(key) for key in L}
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    D = {key:count(key) for key in L}
  File "<pyshell#35>", line 1, in <dictcomp>
    D = {key:count(key) for key in L}
NameError: name 'count' is not defined
>>> D = {key:len(key) for key in L}
>>> D
{'apples': 6, 'coconut': 7, 'giraffe': 7, 'lion': 4}
>>> import collections import Counter
SyntaxError: invalid syntax
>>> from collections import Counter
>>> D = { key:{'len':len(key), 'wh':Counter(key)} for key in L }
>>> D
{'apples': {'len': 6, 'wh': Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1, 's': 1})}, 'coconut': {'len': 7, 'wh': Counter({'c': 2, 'o': 2, 'n': 1, 'u': 1, 't': 1})}, 'giraffe': {'len': 7, 'wh': Counter({'f': 2, 'g': 1, 'i': 1, 'r': 1, 'a': 1, 'e': 1})}, 'lion': {'len': 4, 'wh': Counter({'l': 1, 'i': 1, 'o': 1, 'n': 1})}}
>>> 
>>> 
>>> L = [1, 2, 3, 4]
>>> LC = [ i**2 for i in L if i == 3 ]
>>> LC
[9]
>>> LC = [ i**2 if i == 3 else i for i in L ]
>>> LC
[1, 2, 9, 4]
>>> 
>>> LC = [(x, y) for x in range(10) for y in range(10) if x + y == 9]
>>> LC
[(0, 9), (1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1), (9, 0)]
>>> 
>>> L = list(range(10, 100))
>>> L
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> LC = [x for x in L if int(str(x)[1]) + int(str(x)[0]) == 13]
>>> LC
[49, 58, 67, 76, 85, 94]
>>> [x for x in L if int(str(x)[1]) + int(str(x)[0]) == 13]
[49, 58, 67, 76, 85, 94]

>>> for i in [x**2 for x in range(10)]:
	print(i)

	
0
1
4
9
16
25
36
49
64
81
>>> 
>>> D = {'name':'anil', 'age': 35, 'country':'usa'}
>>> DC = { value:key for key, value in D.items() }
>>> DC
{'anil': 'name', 35: 'age', 'usa': 'country'}
>>> 
