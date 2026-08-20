Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
#dict is mutable ordered heterogenous dynamic size
#list, set, dict cannot be keys
#all datatypes can be values
d={}
type(d)
<class 'dict'>
 d = {1:2,3:4,5:6,7:8}
 
SyntaxError: unexpected indent
KeyboardInterrupt
d = {1:2,3:4,5:6,7:8}
d
{1: 2, 3: 4, 5: 6, 7: 8}
d[1] = 2
d
{1: 2, 3: 4, 5: 6, 7: 8}
d[12.3] = 3
d
{1: 2, 3: 4, 5: 6, 7: 8, 12.3: 3}
del d
d={}
d[1]=1
d
{1: 1}
d[12.3] = 2
d[23+5j] = 3
d['sai']='pavan'
d[True]=False
d[[1,2,3,4]]=4
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d[[1,2,3,4]]=4
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[[1,2,3]] = 4
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d[[1,2,3]] = 4
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[(2,3,4)] = 7
d[{1,2,3}] = 7
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d[{1,2,3}] = 7
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{1:2}] = 2
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d[{1:2}] = 2
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
d[{1:2}] = 2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d[{1:2}] = 2
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
d
{1: False, 12.3: 2, (23+5j): 3, 'sai': 'pavan', (2, 3, 4): 7}
del d
#list set dict cannot be keys
d = {}
d[1] = 1
d[2] = 12.3
d[3] = 12+6j
d[4] = True
KeyboardInterrupt
d[5] = 'str'
d[6] = [1,2,3]
d[7] = (1,2,3)
d[8] = {12,3}
d[9] = {1:2}
d[10] = frozenset(1,2,3)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d[10] = frozenset(1,2,3)
TypeError: frozenset expected at most 1 argument, got 3
d[10] = frozenset({1,2,3})
d
{1: 1, 2: 12.3, 3: (12+6j), 4: True, 5: 'str', 6: [1, 2, 3], 7: (1, 2, 3), 8: {3, 12}, 9: {1: 2}, 10: frozenset({1, 2, 3})}
#all datatypes can be values
#dict operations
#membership only works on keys, not values
del d
d = {'name' : 'nikhil', 'course' : 'PFS' , 'batch' : 65}
d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65}
d['name']
'nikhil'
d.get('name')
'nikhil'
d.get('age')
#difference between accessing value through d[key] and d.get(key) is d.get() does not throw error
d.get('age','key is not there')
'key is not there'
d['course']
'PFS'
d['batch']
65
#membership
'name' in d
True
'age' in d
False
'batch' in d
True
'nikhil' in d
False
#methods
d
{'name': 'nikhil', 'course': 'PFS', 'batch': 65}
d['name'] = 'Saikiran'
d
{'name': 'Saikiran', 'course': 'PFS', 'batch': 65}
d.popitem()
('batch', 65)
d.pop()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.popitem()
('course', 'PFS')
d.pop('course')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    d.pop('course')
KeyError: 'course'
d['phno']=98229378
d
{'name': 'Saikiran', 'phno': 98229378}
d.update({'email':saikiran@codegnan.com,'age':20})
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    d.update({'email':saikiran@codegnan.com,'age':20})
NameError: name 'saikiran' is not defined
d.update({'email':'saikiran@codegnan.com','age':20})
d
{'name': 'Saikiran', 'phno': 98229378, 'email': 'saikiran@codegnan.com', 'age': 20}
d.clear()
d
{}
d = {'name' : 'saikiran', 'course' : 'PFS' , 'batch' : 65}
#we cant modify key in dictionary
id(d)
2128891144704
d.keys()
dict_keys(['name', 'course', 'batch'])

d.values()
dict_values(['saikiran', 'PFS', 65])
sorted(d)
['batch', 'course', 'name']
max(d)
'name'
min(d)
'batch'
len(d)
3
d.items()
dict_items([('name', 'saikiran'), ('course', 'PFS'), ('batch', 65)])
d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65}
d.setdefault('name':'saikiran')
SyntaxError: invalid syntax
d.setdefault('name','saikiran')
'saikiran'
d.setdefault('age','20')
'20'
d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20'}
b=d
b['placed':True]
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    b['placed':True]
KeyError: slice('placed', True, None)
b['placed'] = True
b
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
del n
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    del n
NameError: name 'n' is not defined
del b
a=d.copy()
a
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
del b
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    del b
NameError: name 'b' is not defined
a=d.copy()
a
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
>>> a['placed']=True
>>> a
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
>>> d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
>>> a
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
>>> d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
>>> a
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
>>> d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
>>> a['exam']='attempted'
>>> a
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True, 'exam': 'attempted'}
>>> d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
>>> d.get('name')
'saikiran'
>>> d.get('company','tcs')
'tcs'
>>> d
{'name': 'saikiran', 'course': 'PFS', 'batch': 65, 'age': '20', 'placed': True}
>>> #fromkeys() = initialise multiple key with given value
>>> dict.fromkeys(['python','mysql','flask'],0)
{'python': 0, 'mysql': 0, 'flask': 0}
