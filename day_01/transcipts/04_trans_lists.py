Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LISTS
>>> 
>>> L = ['red', 'green', 'blue', True, False, 12, -12.56, ['a', 'b']]
>>> 
>>> 
>>> # ------------------------ accesability
>>> 
>>> L[0]
'red'
>>> L[-1]
['a', 'b']
>>> L[5]
12
>>> L[-3]
12
>>> L[2:5]
['blue', True, False]
>>> L[::2]
['red', 'blue', False, -12.56]
>>> L[::-1]
[['a', 'b'], -12.56, 12, False, True, 'blue', 'green', 'red']
>>> 
>>> 

>>> # ------------------------- mutable, elements could be replaces
>>> 
>>> L
['red', 'green', 'blue', True, False, 12, -12.56, ['a', 'b']]
>>> L[0]
'red'
>>> L[0] = 'orange'
>>> L
['orange', 'green', 'blue', True, False, 12, -12.56, ['a', 'b']]
>>> del L[-1]
>>> L
['orange', 'green', 'blue', True, False, 12, -12.56]
>>> 
>>> colors = ['pink', 'maroon']
>>> L[1]
'green'
>>> L[1] = colors
>>> L
['orange', ['pink', 'maroon'], 'blue', True, False, 12, -12.56]
>>> 
>>> 
>>> 
>>> L = ['orange', 'green', 'blue', True, False, 12, -12.56]
>>> L
['orange', 'green', 'blue', True, False, 12, -12.56]
>>> colors = ['pink', 'maroon']
>>> L[1]
'green'
>>> L[1] = colors
>>> L
['orange', ['pink', 'maroon'], 'blue', True, False, 12, -12.56]
>>> 
>>> 
>>> L = ['orange', 'green', 'blue', True, False, 12, -12.56]
>>> L[1:3]
['green', 'blue']
>>> L[1:3] = colors
>>> L
['orange', 'pink', 'maroon', True, False, 12, -12.56]
>>> 
>>> 
>>> L = ['orange', 'green', 'blue', True, False, 12, -12.56]
>>> L[0:3]
['orange', 'green', 'blue']
>>> L[0:3] = colors
>>> L
['pink', 'maroon', True, False, 12, -12.56]
>>> 
>>> 
>>> L = ['orange', 'green', 'blue', True, False, 12, -12.56]
>>> L[1]
'green'
>>> L[1:1]
[]
>>> L[1:2]
['green']
>>> L[1:2] = colors
>>> L
['orange', 'pink', 'maroon', 'blue', True, False, 12, -12.56]
>>> 
>>> 
>>> # ------------------------------ operators
\
>>> L1 = ['red', 'green', 'blue']
>>> L2 = ['black', 'grey', 'white']
>>> 
>>> L1 + L2
['red', 'green', 'blue', 'black', 'grey', 'white']
>>> 
>>> L1 * 3
['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue']
>>> 
>>> 'black' in L1 + L2
True
>>> 
>>> len(L1 * 3)
9
>>> del L1
>>> L1
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    L1
NameError: name 'L1' is not defined
>>> L2
['black', 'grey', 'white']
>>> del L[1]
>>> L2
['black', 'grey', 'white']
>>> del L2[1]
>>> L2
['black', 'white']
>>> 
>>> 
>>> # ------------------------------ List operations
>>> 
>>> # adding elements
>>> 
>>> L
['orange', 'maroon', 'blue', True, False, 12, -12.56]
>>> L = ['red', 'green', 'blue']
>>> L.append('yellow')
>>> L
['red', 'green', 'blue', 'yellow']
>>> L.append('maroon')
>>> L
['red', 'green', 'blue', 'yellow', 'maroon']
>>> L.insert(1, 'pink')
>>> L
['red', 'pink', 'green', 'blue', 'yellow', 'maroon']
>>> L.append[1]('grey')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    L.append[1]('grey')
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> L
['red', 'pink', 'green', 'blue', 'yellow', 'maroon']
>>> L2
['black', 'white']
>>> L + L2
['red', 'pink', 'green', 'blue', 'yellow', 'maroon', 'black', 'white']
>>> L
['red', 'pink', 'green', 'blue', 'yellow', 'maroon']
>>> L.extend(L1)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    L.extend(L1)
NameError: name 'L1' is not defined
>>> L.extend(L2)
>>> L
['red', 'pink', 'green', 'blue', 'yellow', 'maroon', 'black', 'white']
>>> 
>>> # --------------------------------------
>>> 
>>> L
['red', 'pink', 'green', 'blue', 'yellow', 'maroon', 'black', 'white']
>>> ['red', 'green', 'blue', True, False, 12, -12.56, ['a', 'b']]
['red', 'green', 'blue', True, False, 12, -12.56, ['a', 'b']]
>>> 
>>> 
>>> L[2]
'green'
>>> L[2]
'green'
>>> L
['red', 'pink', 'green', 'blue', 'yellow', 'maroon', 'black', 'white']
>>> L = ['red', 'green', 'blue', True, False, 12, -12.56, ['a', 'b']]
>>> L[1]
'green'
>>> L[1][2]
'e'
>>> L[1][2] = 'x'
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    L[1][2] = 'x'
TypeError: 'str' object does not support item assignment
>>> L[-1]
['a', 'b']
>>> L[-1][-1]
'b'
>>> L[-1][-1] = 'x'
>>> L
['red', 'green', 'blue', True, False, 12, -12.56, ['a', 'x']]
>>> 

>>> # List is mutable
>>> # The elements inside the list need not be mutable
>>> 
>>> # Treat the elements according to their nature
>>> 
>>> L
['red', 'green', 'blue', True, False, 12, -12.56, ['a', 'x']]
>>> L.pop()
['a', 'x']
>>> L.pop()
-12.56
>>> L
['red', 'green', 'blue', True, False, 12]
>>> L.pop(2)
'blue'
>>> L
['red', 'green', True, False, 12]
>>> L.remove('green')
>>> L
['red', True, False, 12]
>>> 
>>> 
>>> # search
>>> 
>>> L
['red', True, False, 12]
>>> L.index('red')
0
>>> L.count(True)
1
>>> 
>>> # rearrange elements: sort/reverse
>>> 
>>> 
>>> L = ['sheep', 'goat', 'buffalo', 'cow']
>>> reversed(L)
<list_reverseiterator object at 0x0000028CAAC91630>
>>> list(reverse(L))
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    list(reverse(L))
NameError: name 'reverse' is not defined
>>> list(reversed(L))
['cow', 'buffalo', 'goat', 'sheep']
>>> L
['sheep', 'goat', 'buffalo', 'cow']
>>> L.reverse()
>>> L
['cow', 'buffalo', 'goat', 'sheep']
>>> 
>>> L
['cow', 'buffalo', 'goat', 'sheep']
>>> sorted(L)
['buffalo', 'cow', 'goat', 'sheep']
>>> L
['cow', 'buffalo', 'goat', 'sheep']
>>> L.sort()
>>> L
['buffalo', 'cow', 'goat', 'sheep']
>>> 
>>> 
>>> 
>>> # ---------------------------------------- copy
>>> 
>>> L
['buffalo', 'cow', 'goat', 'sheep']
>>> L1 = L
>>> L
['buffalo', 'cow', 'goat', 'sheep']
>>> L1
['buffalo', 'cow', 'goat', 'sheep']
>>> L1.append('camel')
>>> L1
['buffalo', 'cow', 'goat', 'sheep', 'camel']
>>> L
['buffalo', 'cow', 'goat', 'sheep', 'camel']
>>> 
>>> 
>>> L2 = L1[:]
>>> L1
['buffalo', 'cow', 'goat', 'sheep', 'camel']
>>> L2
['buffalo', 'cow', 'goat', 'sheep', 'camel']
>>> L2.append('cat')
>>> L2
['buffalo', 'cow', 'goat', 'sheep', 'camel', 'cat']
>>> L1
['buffalo', 'cow', 'goat', 'sheep', 'camel']
>>> 
>>> L
['buffalo', 'cow', 'goat', 'sheep', 'camel']
>>> L.append(['ant', 'cat', 'dog'])
>>> L
['buffalo', 'cow', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog']]
>>> L3 = L[:]
>>> L2
['buffalo', 'cow', 'goat', 'sheep', 'camel', 'cat']
>>> L3
['buffalo', 'cow', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog']]
>>> L
['buffalo', 'cow', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog']]
>>> L.insert(2, 'giraffe')
>>> L
['buffalo', 'cow', 'giraffe', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog']]
>>> L3
['buffalo', 'cow', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog']]
>>> L3[-1]
['ant', 'cat', 'dog']
>>> L3[-1].append('parrot')
>>> L3
['buffalo', 'cow', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog', 'parrot']]
>>> L
['buffalo', 'cow', 'giraffe', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog', 'parrot']]
>>> 
>>> 
>>> import copy
>>> 
>>> L5 = copy.deepcopy(L)
>>> L5
['buffalo', 'cow', 'giraffe', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog', 'parrot']]
>>> L
['buffalo', 'cow', 'giraffe', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog', 'parrot']]
>>> L[-1].append('pigeon')
>>> L
['buffalo', 'cow', 'giraffe', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog', 'parrot', 'pigeon']]
>>> L5
['buffalo', 'cow', 'giraffe', 'goat', 'sheep', 'camel', ['ant', 'cat', 'dog', 'parrot']]
>>> 
>>> 
>>> #------------------------- iterations
>>> 
>>> for item in L:
	print(item)

	
buffalo
cow
giraffe
goat
sheep
camel
['ant', 'cat', 'dog', 'parrot', 'pigeon']
>>> 
