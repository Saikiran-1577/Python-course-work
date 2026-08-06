Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data Types
#int float complex
a = 99
type(a)
<class 'int'>
b = 3.14
type(b)
<class 'float'>
c = 12+5j
type(c)
<class 'complex'>
s = 78
s += 1
id(s)
140724265012792
s +=1
id(s)
140724265012824
s = "codegnan"
id(s)
2645549926512
s += "python"
s
'codegnanpython'
id(s)
2645507147632
s='abcdefg'
type(s)
<class 'str'>
# str list tuple
l = [1,2,3,4,5,5,6]
l
[1, 2, 3, 4, 5, 5, 6]
type(l)
<class 'list'>
id(l)
2645549893248
l.append(12)
l
[1, 2, 3, 4, 5, 5, 6, 12]
id(l)
2645549893248
l = [1,12.3,34,"str"[1,2,3]]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    l = [1,12.3,34,"str"[1,2,3]]
TypeError: string indices must be integers, not 'tuple'
l
[1, 2, 3, 4, 5, 5, 6, 12]
l = [1,12.3,34,"str",[1,2,3]]
l
[1, 12.3, 34, 'str', [1, 2, 3]]
type(l)
<class 'list'>
t=(1,2,3,4,5)
type(t)
<class 'tuple'>
t
(1, 2, 3, 4, 5)
t = (1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,12.3,4,'c')
t
(1, 12.3, 4, 'c')
>>> # mapping the datatypes
>>> #set dict
>>> s = {80,70,50,46,46,45,78,90,90,90}
>>> s
{80, 50, 70, 78, 90, 45, 46}
>>> id(s)
2645549474176
>>> s.add(20)
>>> s
{80, 50, 20, 70, 78, 90, 45, 46}
>>> id(s)
2645549474176
>>> a={1,12.3,'string'}
>>> a
{1, 'string', 12.3}
>>> type(s)
<class 'set'>
>>> d = {'productname': 'XYZ','prize':876,'stock':True}
>>> d
{'productname': 'XYZ', 'prize': 876, 'stock': True}
>>> s = {1,2,3,4}
>>> s = frozenset({1,1,2,3,4,7,5,23,18})
>>> s
frozenset({1, 2, 3, 4, 5, 7, 18, 23})
>>> a = True
>>> b =False
>>> type(a)
<class 'bool'>
>>> a={}
>>> l=[]
>>> t=()
>>> s=''
>>> s= None
>>> s
>>> type(s)
<class 'NoneType'>
