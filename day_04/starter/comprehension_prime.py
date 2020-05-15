n = int(input('Enter a number: '))



if(any([n % i == 0 for i in range(2, n)])):
    print('The number is not prime')
else:
    print('The number is prime')



# ------------------------- Wenbin

'''
>>> L = [x**2 for x in range(100) if x % 5 == 0]
>>> L
[0, 25, 100, 225, 400, 625, 900, 1225, 1600, 2025, 2500, 3025, 3600, 4225, 4900, 5625, 6400, 7225, 8100, 9025]
>>>
>>>
>>>
>>> [(n % i == 0) for i in range(2, n)]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    [(n % i == 0) for i in range(2, n)]
NameError: name 'n' is not defined
>>> n = 8
>>> [(n % i == 0) for i in range(2, n)]
[True, False, True, False, False, False]
>>> any([(n % i == 0) for i in range(2, n)])
True
>>> all([(n % i == 0) for i in range(2, n)])
False
>>>

'''
