Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from itertools import permutations, combinations
>>> 
>>> L = ['a', 'd', 'c', 'b']
>>> c = list(permutations(L, 3))
>>> c
[('a', 'd', 'c'), ('a', 'd', 'b'), ('a', 'c', 'd'), ('a', 'c', 'b'), ('a', 'b', 'd'), ('a', 'b', 'c'), ('d', 'a', 'c'), ('d', 'a', 'b'), ('d', 'c', 'a'), ('d', 'c', 'b'), ('d', 'b', 'a'), ('d', 'b', 'c'), ('c', 'a', 'd'), ('c', 'a', 'b'), ('c', 'd', 'a'), ('c', 'd', 'b'), ('c', 'b', 'a'), ('c', 'b', 'd'), ('b', 'a', 'd'), ('b', 'a', 'c'), ('b', 'd', 'a'), ('b', 'd', 'c'), ('b', 'c', 'a'), ('b', 'c', 'd')]
>>> ''.join(('a', 'd', 'c'))
'adc'
>>> words = []
>>> for item in c:
	words.append(''.join(item))

	
>>> words
['adc', 'adb', 'acd', 'acb', 'abd', 'abc', 'dac', 'dab', 'dca', 'dcb', 'dba', 'dbc', 'cad', 'cab', 'cda', 'cdb', 'cba', 'cbd', 'bad', 'bac', 'bda', 'bdc', 'bca', 'bcd']
>>> c = list(combinations(L, 3))
>>> c
[('a', 'd', 'c'), ('a', 'd', 'b'), ('a', 'c', 'b'), ('d', 'c', 'b')]
>>> 
>>> # --------------------------------------------- collections
>>> 
>>> from collections import Counter
>>> 
>>> 
>>> text = 'example'
>>> D = {}
>>> for c in text:
	if c in D.keys():
		D[c] = D[c] + 1
	else:
		D[c] = 1

		
>>> D
{'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1}
>>> z = Counter(text)
>>> z
Counter({'e': 2, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1})
>>> 
