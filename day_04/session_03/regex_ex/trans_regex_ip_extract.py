Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import subprocess
>>> content = subprocess.check_output('ipconfig -all', shell=True)
>>> content = content.decode()
>>> type(content)
<class 'str'>
>>>
>>> # ip address ---> 192.168.34.2
>>>
>>> pattern = "(\d{1,3}\.){3}\d{1,3}"
>>>
>>> import re
>>> ips = re.findall(pattern, content)
>>> ips
['17.', '255.', '17.', '255.', '255.', '255.', '255.', '0.', '255.', '0.', '0.', '0.']
>>> pattern = r"(\d{1,3}\.){3}\d{1,3}"
>>> re.findall(pattern, content)
['17.', '255.', '17.', '255.', '255.', '255.', '255.', '0.', '255.', '0.', '0.', '0.']
>>> pattern
'(\\d{1,3}\\.){3}\\d{1,3}'
>>> pattern = r"(\d{1,3}\.){3}(\d{1,3})"
>>> re.findall(pattern, content)
[('17.', '1'), ('255.', '0'), ('17.', '254'), ('255.', '1'), ('255.', '0'), ('255.', '254'), ('255.', '2'), ('0.', '101'), ('255.', '0'), ('0.', '1'), ('0.', '1'), ('0.', '1')]

>>> pattern = r"(\d{1,3}\.){3}(\d{1,3})"
>>> re.search(pattern, test)
<re.Match object; span=(29, 41), match='192.168.17.1'>
>>> re.findall(pattern, test)
[('17.', '1')]
>>> mobjs = re.finditer(pattern, test)
>>> for obj in mobjs:
	print(obj.group(), obj.span())


192.168.17.1 (29, 41)
>>> mobjs = re.finditer(pattern, content)
>>> for obj in mobjs:
	print(obj.group(), obj.span())


192.168.17.1 (1860, 1872)
255.255.255.0 (1925, 1938)
192.168.17.254 (2142, 2156)
192.168.255.1 (2958, 2971)
255.255.255.0 (3024, 3037)
192.168.255.254 (3241, 3256)
192.168.255.2 (3606, 3619)
192.168.0.101 (4107, 4120)
255.255.255.0 (4173, 4186)
192.168.0.1 (4417, 4428)
192.168.0.1 (4469, 4480)
192.168.0.1 (4653, 4664)
>>>

>>> # Lease Expires . . . . . . . . . . : 15 May 2020 04:40:36
>>>
>>> pattern = r"(Lease Expires).*(\d{1,2}\s\w*\s\d{4})\s(\d{2}:\d{2}:\d{2})"
>>> test = "Lease Expires . . . . . . . . . . : 15 May 2020 04:40:36"
>>> re.search(pattern, test)
<re.Match object; span=(0, 56), match='Lease Expires . . . . . . . . . . : 15 May 2020 0>
>>> re.search(pattern, content)
<re.Match object; span=(2004, 2060), match='Lease Expires . . . . . . . . . . : 15 May 2020 0>
>>> Lease Expires . . . . . . . . . . : 15 May 2020 04:40:36
SyntaxError: invalid syntax
>>>
>>> re.search(pattern, content).group()
'Lease Expires . . . . . . . . . . : 15 May 2020 04:40:36'
>>> for m in re.finditer(pattern, content):
	print(m.group())


Lease Expires . . . . . . . . . . : 15 May 2020 04:40:36
Lease Expires . . . . . . . . . . : 15 May 2020 04:40:36
Lease Expires . . . . . . . . . . : 22 May 2020 04:14:45


# ----------------------------

Reference fro mwww.regex101.com

pattern = r"\w*@\w*\.(com|in|org)"
test = "My name is Purushotham and my email is contact@mindfullearning.in and my phone number is +9187654323"

re.search(pattern, test).group()
