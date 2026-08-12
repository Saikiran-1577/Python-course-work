Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Tuple
#collection of elements enclosed in a parenthesis and it is immutable
t = ()
t = tuple()
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t = (1)
t
1
t = (1,)
t
(1,)
t = (1,1,1,1)
t
(1, 1, 1, 1)
t = (1,23.5,'str',[1,23],(1,2,3),{1,2,3},{1:2,2:3,4:3},True,5+7j)
t
(1, 23.5, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 2, 2: 3, 4: 3}, True, (5+7j))
type(t)
<class 'tuple'>
#tuple allows duplicates and it is heterogenic
#operations of tuple
#concatination

9
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 23.5, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 2, 2: 3, 4: 3}, True, (5+7j))
t[1]
23.5
t[2]
'str'
t[]6
SyntaxError: invalid syntax
t[6]
{1: 2, 2: 3, 4: 3}
t[-1]
(5+7j)
t[::-1]
((5+7j), True, {1: 2, 2: 3, 4: 3}, {1, 2, 3}, (1, 2, 3), [1, 23], 'str', 23.5, 1)
t[-1:-3:-1]
((5+7j), True)
t[-3]
{1: 2, 2: 3, 4: 3}
t[-2]
True
t[1:6]
(23.5, 'str', [1, 23], (1, 2, 3), {1, 2, 3})
23.4 in t
False
23.5 in t
True
False in t
False
True in t
True
#BUilt in Functions
t = (1,12,34,23,45,67,89,56,76)
t
(1, 12, 34, 23, 45, 67, 89, 56, 76)
sorted(t)
[1, 12, 23, 34, 45, 56, 67, 76, 89]
max(t)
89
min(t)
1
len(t)
9
t
(1, 12, 34, 23, 45, 67, 89, 56, 76)
t.index(67)
5
t.index(76)
8
sort(t)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    sort(t)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
t
(1, 12, 34, 23, 45, 67, 89, 56, 76)
all((1,2,3))
True
any((1,2,3,00,0))
True
all((1,2,3,00,0))
False
t=1,2,3
1
1
t
(1, 2, 3)
a,b,c=t
a
1
b
2
c
3
t
(1, 2, 3)
t = (1,2,3,4,[4,5,6],6)
t
(1, 2, 3, 4, [4, 5, 6], 6)
t[4]
[4, 5, 6]
t[4].append(7)
t[]4[
    
SyntaxError: '[' was never closed
t[4]
[4, 5, 6, 7]
t
(1, 2, 3, 4, [4, 5, 6, 7], 6)
t
(1, 2, 3, 4, [4, 5, 6, 7], 6)
t=(1,2,34,54,45,65)
sum(t)
201
t
(1, 2, 34, 54, 45, 65)
#set
#set is mutable,unordered,dynamical,heterogenous uni
s = set()
type(s)
<class 'set'>
#set does not allow duplicates
s = {1,2,3,4,234,2345,6542,798,284,345}
#set does not allow mutable elements
s
{1, 2, 3, 4, 2345, 234, 6542, 345, 284, 798}
s = {1,1,1,1,}
s
{1}
s = set(1)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s = set(1)
TypeError: 'int' object is not iterable
s = set()
s.add(1)
s.add(23.5)
s.add('str
      
SyntaxError: unterminated string literal (detected at line 1)
s.add('str')
      
s.add(5+8j)
      
s
      
{1, (5+8j), 'str', 23.5}
s.add([1,2,3])
      
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add((1,2,3,4))
      
s.add({1,2,3,4})
      
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
a
      
1
s
      
{1, 'str', (1, 2, 3, 4), 23.5, (5+8j)}
s.add({1:1,2:2,3:3})
      
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s.add({1:1,2:2,3:3})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(tuple(1,3,5,6))
      
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s.add(tuple(1,3,5,6))
TypeError: tuple expected at most 1 argument, got 4
s.add((1,3,5,6))
      
s
      
{1, 'str', (1, 2, 3, 4), 23.5, (5+8j), (1, 3, 5, 6)}
s.add(False)
      
s
      
{False, 1, 'str', (1, 2, 3, 4), 23.5, (5+8j), (1, 3, 5, 6)}
#set operations
      
s
      
{False, 1, 'str', (1, 2, 3, 4), 23.5, (5+8j), (1, 3, 5, 6)}
{1,23}+{1,2}
      
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    {1,23}+{1,2}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
{1,2}*2
      
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    {1,2}*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
s[0]
      
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[::2}
      
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s[::2]
      
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    s[::2]
TypeError: 'set' object is not subscriptable
a = {1,2,3,4,5}
      
b = {3,5,6,7,2,}
      
b = {3,4,5,6,2,4}
      
2 in a
      
True
10 not in a
      
True
a | b
      
{1, 2, 3, 4, 5, 6}
a & b
      
{2, 3, 4, 5}
a-b
      
{1}
b - a
      
{6}
a ^b
      
{1, 6}
a
      
{1, 2, 3, 4, 5}
{1}<=a
      
True
{1,2,3}<=a
      
True
{3,4,5}<=a
      
True
a>={1,2,3}
      
True
a>={6,7,8}
      
False
m={1,2,3}
      
n={4,5,6}
      
n.isdisjoint(m)
      
True
a.isdisjoint(b)
      
False
a
      
{1, 2, 3, 4, 5}
a = {1,2,34,63,78,12,45,74}
      
a
      
{1, 2, 34, 74, 12, 45, 78, 63}
sorted(a)
      
[1, 2, 12, 34, 45, 63, 74, 78]
max(a)
      
78
min(a)
      
1
len(a)
      
8
a.index(a)
      
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
a.index(4)
      
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    a.index(4)
AttributeError: 'set' object has no attribute 'index'
all({1,2,3,4,2,1,})
      
True
any({12,0,34,0,00})
      
True
any({0,(),[],''})
      
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    any({0,(),[],''})
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
any({0,(),''})
      
False
sum(a)
      
309
a
      
{1, 2, 34, 74, 12, 45, 78, 63}
a = {1,2,3}
      
b = a
      
b.add(4)
      
a
      
{1, 2, 3, 4}
b
      
{1, 2, 3, 4}
c = a.copy()
      
a
      
{1, 2, 3, 4}
c
      
{1, 2, 3, 4}
c.add(5)
      
c
      
{1, 2, 3, 4, 5}
a
      
{1, 2, 3, 4}
a.add(6)
      
a
      
{1, 2, 3, 4, 6}
a.add(56)
      
a
      
{1, 2, 3, 4, 6, 56}
a.add(10)
      
a
      
{1, 2, 3, 4, 6, 10, 56}
a.update({12,22,33,44})
      
a
      
{1, 2, 3, 4, 33, 6, 10, 12, 44, 22, 56}
a.pop()
      
1
a.remove(10)
      
a
      
{2, 3, 4, 33, 6, 12, 44, 22, 56}
>>> a.remove(33)
...       
>>> a
...       
{2, 3, 4, 6, 12, 44, 22, 56}
>>> a.discard(100)
...       
>>> a.discard(5)
...       
>>> a
...       
{2, 3, 4, 6, 12, 44, 22, 56}
>>> a.discard(6)
...       
>>> a
...       
{2, 3, 4, 12, 44, 22, 56}
>>> a
...       
{2, 3, 4, 12, 44, 22, 56}
>>> a.clear
...       
<built-in method clear of set object at 0x00000252E8837220>
>>> a
...       
{2, 3, 4, 12, 44, 22, 56}
>>> a.clear()
...       
>>> a
...       
set()
>>> a = frozenset({1,2,3,4})
...       
>>> a
...       
frozenset({1, 2, 3, 4})
