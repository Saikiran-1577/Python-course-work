Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[]
l = list()
type(l)
<class 'list'>
list= [1,5.4,'str',True,[1,23,4,5],(1,2,3),{1,2,45},{1:1,2:4,3:9},3+9j]
l
[]
list
[1, 5.4, 'str', True, [1, 23, 4, 5], (1, 2, 3), {1, 2, 45}, {1: 1, 2: 4, 3: 9}, (3+9j)]
l=[1,2,1,2,2,2,1,1]
l
[1, 2, 1, 2, 2, 2, 1, 1]
a = [1,2,3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a = [1,2,3]
b = [4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*2
[1, 2, 3, 1, 2, 3]
a=[123,456,789,127]
a[1]
456
a[4]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[4]
IndexError: list index out of range
a[3]
127
a[-1]
127
a[:-1]
[123, 456, 789]
a.add[124,345,642,234]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.add[124,345,642,234]
AttributeError: 'list' object has no attribute 'add'
a.apprnd[124,345,642,234]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.apprnd[124,345,642,234]
AttributeError: 'list' object has no attribute 'apprnd'. Did you mean: 'append'?
a.append[124,345,642,234]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.append[124,345,642,234]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.append(124,345,642,234)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.append(124,345,642,234)
TypeError: list.append() takes exactly one argument (4 given)
a.append(124)
a.append(456)
a
[123, 456, 789, 127, 124, 456]
a[-1:-4:-1]
[456, 124, 127]
a[;4]
SyntaxError: invalid syntax
a[:4]
[123, 456, 789, 127]
a[:-1]
[123, 456, 789, 127, 124]
a[:2]
[123, 456]
123 in a
True
123 not in a
False
564 in a
False
980 not in a
True
567 in a
False
7656 not in a
True
#list methods
a
[123, 456, 789, 127, 124, 456]
max(a)
789
min(a)
123
len(a)
6
sorted(a)
[123, 124, 127, 456, 456, 789]
a
[123, 456, 789, 127, 124, 456]
id(a)
1867615737920
a[0]=12
a
[12, 456, 789, 127, 124, 456]
id(a)
1867615737920
a[1]=13
a
[12, 13, 789, 127, 124, 456]
a[2]=14
a
[12, 13, 14, 127, 124, 456]
a[3]=15
a
[12, 13, 14, 15, 124, 456]
id(a)
1867615737920
a.append(16)
a
[12, 13, 14, 15, 124, 456, 16]
a[4]=17
a
[12, 13, 14, 15, 17, 456, 16]
a[5]=18
a
[12, 13, 14, 15, 17, 18, 16]
a.append(20)
a
[12, 13, 14, 15, 17, 18, 16, 20]
a.insert(23)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.insert(23)
TypeError: insert expected 2 arguments, got 1
a.insert(6,23)
a
[12, 13, 14, 15, 17, 18, 23, 16, 20]
a.extend([1,2,3,4])
a
[12, 13, 14, 15, 17, 18, 23, 16, 20, 1, 2, 3, 4]
a.pop()
4
a.pop()
3
a.pop(5)
18
a.pop(5)
23
a
[12, 13, 14, 15, 17, 16, 20, 1, 2]
a.pop(2)
14
a
[12, 13, 15, 17, 16, 20, 1, 2]
id(a)
1867615737920
a[2]=45
del a[1:5]
a
[12, 20, 1, 2]
#pop() is used to delete the value based on index
#updating
a[4]=87
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a[4]=87
IndexError: list assignment index out of range
a[1]=1
a
[12, 1, 1, 2]
a = b
b
[4, 5, 6]
a
[4, 5, 6]
id(a)
1867615738368
>>> id(b)
1867615738368
>>> a.append(2)
>>> a
[4, 5, 6, 2]
>>> b
[4, 5, 6, 2]
>>> a.index(5)
1
>>> a
[4, 5, 6, 2]
>>> a.count(2)
1
>>> a.clear()
>>> a
[]
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b = [1,2,3,4,2,3,4]
>>> sorted(b)
[1, 2, 2, 3, 3, 4, 4]
>>> b.sort
<built-in method sort of list object at 0x000001B2D6963400>
>>> b.sort()
>>> b
[1, 2, 2, 3, 3, 4, 4]
>>> b.count(3)
2
>>> any([1,'',False,[],(),{},set()])
True
>>> any([0,'',False,[],(),{},set()])
False
