Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Type conversion
a = 20
float(a)
20.0
str(a)
'20'
complex(a)
(20+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
#float to other
b = 12.3
int(b)
12
str(b)
'12.3'
complex(b)
(12.3+0j)
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
#str to other
s = 'codegnan'
c = '67895479'
int(s)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
int(c)
67895479
float(s)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
float(c)
67895479.0
list(c)
['6', '7', '8', '9', '5', '4', '7', '9']
tuple(c)
('6', '7', '8', '9', '5', '4', '7', '9')
set(c)
{'5', '7', '8', '9', '4', '6'}
set(s)
{'n', 'e', 'a', 'g', 'c', 'o', 'd'}
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
complex(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
complex(c)
(67895479+0j)
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
dict(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(c)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
#complex to other
c = 10+5j
int(c)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+5j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
#list to other
l = [1,2,3,4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
l
[1, 2, 3, 4, 5]
complex(l)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
str(l)
'[1, 2, 3, 4, 5]'
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
#tuple to others
t = (2,3,4,5,6)
t
(2, 3, 4, 5, 6)
int(t)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(t)
'(2, 3, 4, 5, 6)'
set(l)
{1, 2, 3, 4, 5}
list(t)
[2, 3, 4, 5, 6]
dict(l)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
complex(l)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
#set to others
s = {2,3,4,5,6,7}
s
{2, 3, 4, 5, 6, 7}
int (s)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    int (s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    complex(s)
TypeError: complex() argument must be a string or a number, not set
list(s)
[2, 3, 4, 5, 6, 7]
tuple(s)
(2, 3, 4, 5, 6, 7)
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(s)
True
>>> #dict to others
>>> d ={1:1,2:2,3:3}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    complex(d)
TypeError: complex() argument must be a string or a number, not dict
>>> str()d
SyntaxError: invalid syntax
>>> str(d)
'{1: 1, 2: 2, 3: 3}'
>>> list(d)
[1, 2, 3]
>>> tuple(d)
(1, 2, 3)
>>> set(d)
{1, 2, 3}
>>> bool(d)
True
