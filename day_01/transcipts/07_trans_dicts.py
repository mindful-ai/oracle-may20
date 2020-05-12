Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # DICTIONARIES
>>> 
>>> 
>>> # record => 'anil', '35, 'India', 'Oracle', 'USA'
>>> 
>>> s = {'anil', '35', 'India', 'Oracle', 'USA'}
>>> s
{'USA', 'anil', '35', 'India', 'Oracle'}
>>> T = ('anil', '35', 'India', 'Oracle', 'USA')
>>> # 0 -> name, 1 -> age, 2 -> country of birth..
>>> T[0]
'anil'
>>> L = ['anil', '35', 'India', 'Oracle', 'USA']
>>> L[0]
'anil'
>>> D = { 'name':'anil', 'age':35, 'country':'India', 'company':'Oracle' }
>>> D['name']
'anil'
>>> D['dob'] = '19/9/2020'
>>> D
{'name': 'anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'dob': '19/9/2020'}
>>> 
>>> 
>>> 
>>> D['salary']
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    D['salary']
KeyError: 'salary'
>>> D['salary'] = '400000 USD'
>>> D
{'name': 'anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'dob': '19/9/2020', 'salary': '400000 USD'}
>>> D.setdefault('addr','bangalore')
'bangalore'
>>> D
{'name': 'anil', 'age': 35, 'country': 'India', 'company': 'Oracle', 'dob': '19/9/2020', 'salary': '400000 USD', 'addr': 'bangalore'}
>>> 
>>> 
>>> 
>>> D.pop('age')
35
>>> D
{'name': 'anil', 'country': 'India', 'company': 'Oracle', 'dob': '19/9/2020', 'salary': '400000 USD', 'addr': 'bangalore'}
>>> D.pop()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    D.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d1 = {'languages':['English'], 'age':35}
>>> d1
{'languages': ['English'], 'age': 35}
>>> D.update(d1)
>>> D
{'name': 'anil', 'country': 'India', 'company': 'Oracle', 'dob': '19/9/2020', 'salary': '400000 USD', 'addr': 'bangalore', 'languages': ['English'], 'age': 35}
>>> D['country']
'India'
>>> D['country'] ='USA'
>>> D
{'name': 'anil', 'country': 'USA', 'company': 'Oracle', 'dob': '19/9/2020', 'salary': '400000 USD', 'addr': 'bangalore', 'languages': ['English'], 'age': 35}
>>> D['languages']
['English']
>>> D['languages'].append('Spanish')
>>> D
{'name': 'anil', 'country': 'USA', 'company': 'Oracle', 'dob': '19/9/2020', 'salary': '400000 USD', 'addr': 'bangalore', 'languages': ['English', 'Spanish'], 'age': 35}
>>> 
>>> 
>>> D.keys()
dict_keys(['name', 'country', 'company', 'dob', 'salary', 'addr', 'languages', 'age'])
>>> D.values()
dict_values(['anil', 'USA', 'Oracle', '19/9/2020', '400000 USD', 'bangalore', ['English', 'Spanish'], 35])
>>> D.items()
dict_items([('name', 'anil'), ('country', 'USA'), ('company', 'Oracle'), ('dob', '19/9/2020'), ('salary', '400000 USD'), ('addr', 'bangalore'), ('languages', ['English', 'Spanish']), ('age', 35)])
>>> 
