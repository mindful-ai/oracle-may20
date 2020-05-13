Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Purushotham\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.chdir(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts")
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts'
>>> os.listdir()
['09_trans_loops.py', '13_file_io.py', '14_special_functions.py', '15_special_modules_2.py', 'lyrics.txt', 'lyrics2.txt', 'whreport.txt']
>>> for file in os.listdir():
	if(file.endswith('txt')):
		print(file)

		
lyrics.txt
lyrics2.txt
whreport.txt
>>> os.mkdir('textfiles')
>>> os.chdir('textfiles')
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts\\textfiles'
>>> os.chdir(os.pardir)
>>> os.getcwd()
'C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts'
>>> 
>>> import shutil
>>> shutil.copy('lyrics.txt', 'textfiles\lyrics.txt')
'textfiles\\lyrics.txt'
>>> dstpath = 'textfiles'
>>> os.path.join(dstpath, 'lyrics.txt')
'textfiles\\lyrics.txt'
>>> 
>>> 
>>> for file in os.listdir():
	if(file.endswith('txt')):
		shutil.copy(file, os.path.join(dstpath, file))

		
'textfiles\\lyrics.txt'
'textfiles\\lyrics2.txt'
'textfiles\\whreport.txt'
>>> 
>>> 
>>> # --------------------------------- subprocess
>>> 
>>> import subprocess
>>> 
>>> subprocess.call('dir', shell=True)
0
>>> content = subprocess.check_output('dir', shell=True)
>>> print(content)
b' Volume in drive C is Windows\r\n Volume Serial Number is 68CD-4284\r\n\r\n Directory of C:\\Users\\Purushotham\\Desktop\\oracle\\day_02\\transcripts\r\n\r\n13-05-2020  02:49    <DIR>          .\r\n13-05-2020  02:49    <DIR>          ..\r\n12-05-2020  21:37             5,498 09_trans_loops.py\r\n12-05-2020  23:30             9,089 13_file_io.py\r\n13-05-2020  00:38             7,442 14_special_functions.py\r\n13-05-2020  02:46             1,506 15_special_modules_2.py\r\n12-05-2020  23:08             1,796 lyrics.txt\r\n12-05-2020  23:25             1,888 lyrics2.txt\r\n13-05-2020  02:54    <DIR>          textfiles\r\n12-05-2020  23:57             6,795 whreport.txt\r\n               7 File(s)         34,014 bytes\r\n               3 Dir(s)  304,642,478,080 bytes free\r\n'
>>> type(content)
<class 'bytes'>
>>> content = content.decode()
>>> type(content)
<class 'str'>
>>> print(content)
 Volume in drive C is Windows
 Volume Serial Number is 68CD-4284

 Directory of C:\Users\Purushotham\Desktop\oracle\day_02\transcripts

13-05-2020  02:49    <DIR>          .
13-05-2020  02:49    <DIR>          ..
12-05-2020  21:37             5,498 09_trans_loops.py
12-05-2020  23:30             9,089 13_file_io.py
13-05-2020  00:38             7,442 14_special_functions.py
13-05-2020  02:46             1,506 15_special_modules_2.py
12-05-2020  23:08             1,796 lyrics.txt
12-05-2020  23:25             1,888 lyrics2.txt
13-05-2020  02:54    <DIR>          textfiles
12-05-2020  23:57             6,795 whreport.txt
               7 File(s)         34,014 bytes
               3 Dir(s)  304,642,478,080 bytes free

>>> 
