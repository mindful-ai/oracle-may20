
C:\Users\Purushotham>python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.__version__
'1.9'
>>> exit()

C:\Users\Purushotham>oracle\Scripts\activate.bat

(oracle) C:\Users\Purushotham>python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.__version__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'django' has no attribute '__version__'
>>> exit()

(oracle) C:\Users\Purushotham>pip install django
Collecting django
  Downloading https://files.pythonhosted.org/packages/9d/04/04abb097c84c770180eeebe7ed920ce42f9917ab5ad4de01ff8ed11bc25b/Django-3.0.6-py3-none-any.whl (7.5MB)
    100% |████████████████████████████████| 7.5MB 2.2MB/s
Collecting sqlparse>=0.2.2 (from django)
  Downloading https://files.pythonhosted.org/packages/85/ee/6e821932f413a5c4b76be9c5936e313e4fc626b33f16e027866e1d60f588/sqlparse-0.3.1-py2.py3-none-any.whl (40kB)
    100% |████████████████████████████████| 40kB 2.6MB/s
Collecting pytz (from django)
  Downloading https://files.pythonhosted.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl (510kB)
    100% |████████████████████████████████| 512kB 138kB/s
Collecting asgiref~=3.2 (from django)
  Downloading https://files.pythonhosted.org/packages/68/00/25013f7310a56d17e1ab6fd885d5c1f216b7123b550d295c93f8e29d372a/asgiref-3.2.7-py2.py3-none-any.whl
Installing collected packages: sqlparse, pytz, asgiref, django
Successfully installed asgiref-3.2.7 django-3.0.6 pytz-2020.1 sqlparse-0.3.1
You are using pip version 19.0.3, however version 20.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

(oracle) C:\Users\Purushotham>python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.__version__
'3.0.6'
>>> exit()

(oracle) C:\Users\Purushotham>