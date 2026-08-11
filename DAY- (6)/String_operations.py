Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#trimming methods
s = '      Hello   World             '
s.strip()
'Hello   World'
s.lstrip()
'Hello   World             '
s.rstrip()
'      Hello   World'
s.replace(' ','')
'HelloWorld'
#string
s='saikiran'
del s
fname = 'saikiran'
lname = 'badala'
fname + lname
'saikiranbadala'
fname * 10
'saikiransaikiransaikiransaikiransaikiransaikiransaikiransaikiransaikiransaikiran'
type(fname)
<class 'str'>
name = fname.concat(lname)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name = fname.concat(lname)
AttributeError: 'str' object has no attribute 'concat'
names = 'sai prasad nikhil bunny tarun'
names[0]
's'
names[7]
's'
#slicing
names[:7]
'sai pra'
names[3:17]
' prasad nikhil'
names[13:17]
'khil'
names[13:27]
'khil bunny tar'
names[:-1]
'sai prasad nikhil bunny taru'
#split
s = 'java-pyhton-flask-mysql-fastapi-c'
s.split('-')
['java', 'pyhton', 'flask', 'mysql', 'fastapi', 'c']
s.split('-',2)
['java', 'pyhton', 'flask-mysql-fastapi-c']
s.rsplit('-',2)
['java-pyhton-flask-mysql', 'fastapi', 'c']
l='''python'''
l='''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
c=['python', 'java', 'mysql', 'flask']
''.join(c)
'pythonjavamysqlflask'
' '.join(c)
'python java mysql flask'
' , '.join(c)
'python , java , mysql , flask'
'@'.join(c)
'python@java@mysql@flask'
'-'.join(('1','2','3'))
'1-2-3'
'-'.join({'1','2','3'})
'2-1-3'
a = 'strings.py.java.png.txt'
s
'java-pyhton-flask-mysql-fastapi-c'
a
'strings.py.java.png.txt'
a.partition('.')
('strings', '.', 'py.java.png.txt')
a.partition(' . ')
('strings.py.java.png.txt', '', '')
a.rpartition('.')
('strings.py.java.png', '.', 'txt')
s.rpartition('-')
('java-pyhton-flask-mysql-fastapi', '-', 'c')
#membership
"sai" in names
True
'prasad' not in names
False
#ASCII value
ord('a')
97
chr(97)
'a'
#len
len(names)
29
sorted(names)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'b', 'd', 'h', 'i', 'i', 'i', 'k', 'l', 'n', 'n', 'n', 'n', 'p', 'r', 'r', 's', 's', 't', 'u', 'u', 'y']
#max
max(names)
'y'
#min
min(names)
' '
chr(345)
'ř'
chr(4323)
'უ'
ord(h)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    ord(h)
NameError: name 'h' is not defined
ord('h')
104
#case conversion
#uppercase
a = 'codegnan'
a.upper()
'CODEGNAN'
#lowercase

a.lowercase()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.lowercase()
AttributeError: 'str' object has no attribute 'lowercase'

a.lower()
'codegnan'
a.title
<built-in method title of str object at 0x0000019A7C9476F0>
a.title()
'Codegnan'
a.capitalize()
'Codegnan'
a.swapcase()
'CODEGNAN'
a.casefold()
'codegnan'
a.center()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.center()
TypeError: center expected at least 1 argument, got 0
#testing methods
a='strings.png'
a.startswith('str')
True
a.startswith('list')
False
a.endswith('.png')
True
>>> a.endswith('.py')
False
>>> 'pythnv.13'.islower()
True
>>> 'Pythnv.23'.islower
<built-in method islower of str object at 0x0000019A7C9446B0>
>>> 'Pythnv.23'.islower()
False
>>> 'Pythnv.23'.isupper()
False
>>> 'PYTHON'.isupper()
True
>>> 'PYTHON!#$%@&&%$@&('.isupper()
True
>>> 'saikiran'.isalpha()
True
>>> True
True
>>> 'saikiran'.isalnum()
True
>>> 'saikiran123456'.isalnum()
True
>>> 'sedfrectgs'.isalnum()
True
>>> 'HELLO world'.istitle()
False
>>> 'HELLO'.istitle()
False
>>> 'Hlo Wor'.istitle()
True
>>> 'my_vAR'.isidentifier()
True
>>> "my@var".isidentifier()
False
>>> a.partition('.')
('strings', '.', 'png')
