Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int float complex str list tuple set dict bool
#input formatting
a = input()
codegnan
a
'codegnan'
a = input()
1234
a
'1234'
a = input("Enter the value: ")
Enter the value: ABcdefg890395
a
'ABcdefg890395'
narks = input("Enter the marks:")
Enter the marks:98
narks
'98'
dob = int(input("ENter the DOB:"))
ENter the DOB:2006
dob
2006
cgpa = float(input("Enter the Cgpa:"))
Enter the Cgpa:7.8
cgpa
7.8
names = input("Enter the names:")
Enter the names:Sai kiran bunny prasad nikhil
names
'Sai kiran bunny prasad nikhil'
names.split()
['Sai', 'kiran', 'bunny', 'prasad', 'nikhil']
names = input("Enter the names:").split()
Enter the names:prasad nikhil sai bunny tarun
names
['prasad', 'nikhil', 'sai', 'bunny', 'tarun']
names = tuple(input("Enter the names:").split())
Enter the names:sai bunny prasad tarun nikhil
names
('sai', 'bunny', 'prasad', 'tarun', 'nikhil')
names.split('-')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    names.split('-')
AttributeError: 'tuple' object has no attribute 'split'
names = set(input("enter the names:"))
enter the names:sai prasad '
names
{'a', "'", 'i', 's', 'p', ' ', 'd', 'r'}
names = set(input("enter the names:"))
enter the names:"sai prasad"
names
{'"', 'a', 'i', 's', 'p', ' ', 'd', 'r'}
names = set(input("enter the names:").split())
enter the names:"sai prasad"
names
{'"sai', 'prasad"'}
names = set(input("enter the names:").split())enter the names:"sai prasad"
SyntaxError: invalid syntax
names = set(input("enter the names:").split())
enter the names:
    "sai prasad"
names
set()
marks = input().split()
23 45 67 89 35
SyntaxError: invalid syntax
marks = input().split()
45 65 56 76 89
marks
['45', '65', '56', '76', '89']
map(int,marks)
<map object at 0x00000198F2A05F40>
list(map(int,marks))
[45, 65, 56, 76, 89]
marks = list(map(int,input("Enter the marks:").split()))
Enter the marks:87 58 94 25 26 49 42 
marks
[87, 58, 94, 25, 26, 49, 42]
cgpa = tuple(map(float,input("Enter the cgpa:").split()))
Enter the cgpa:7.8 8.9 6.7 9.9
cgoa
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    cgoa
NameError: name 'cgoa' is not defined. Did you mean: 'cgpa'?
cgpa
(7.8, 8.9, 6.7, 9.9)
players = set(map(int,input("Enter the no of players:").split()))
Enter the no of players:1
players = set(map(int,input("Enter the no of players:").split()))
Enter the no of players:12 18 7 43 67
players
{67, 7, 43, 12, 18}
 a,b=[1,2]
 
SyntaxError: unexpected indent
a
'ABcdefg890395'
a,b=[1,2]
a
1
b
2
a,b,c=(1,12.3,"str")
a
1
b
12.3
c
'str'
email,password = input("Enter the email, password :").split())
SyntaxError: unmatched ')'
email,password = input("Enter the email, password :").split()
Enter the email, password :saikiran@gamil.com 9182393808
email
'saikiran@gamil.com'
passwors
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    passwors
NameError: name 'passwors' is not defined. Did you mean: 'password'?
password
'9182393808'
name , marks = input("Enter the name and marks:").split()
Enter the name and marks:saikiran 65 45 67 87 88
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    name , marks = input("Enter the name and marks:").split()
ValueError: too many values to unpack (expected 2, got 6)
name , marks = input("Enter the name and marks:").split()
Enter the name and marks:saikiran 56
name
'saikiran'
marks
'56'
int(marks)
56
a,b,c=list(map(int,input().split()))
34 56 99
a
34
b
56
c
99
status = eval(input())
true
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
status = eval(input())
True
status
True
type(status)
<class 'bool'>
>>> status = eval(input())
2+5j
>>> status
(2+5j)
>>> type(status)
<class 'complex'>
>>> status = eval(input())
45
>>> status
45
>>> type(status)
<class 'int'>
>>> marks = eval(input())
[1,2,3,4]
>>> marks
[1, 2, 3, 4]
>>> type(marks)
<class 'list'>
>>> marks = eval(input())
(2,3,4,5,6)
>>> marks
(2, 3, 4, 5, 6)
>>> type(marks)
<class 'tuple'>
>>> marks = eval(input())
{3,4,5,6,3}
>>> marks
{3, 4, 5, 6}
>>> type(marks)
<class 'set'>
>>> status = eval(input())
{1:1,2:2,3:3}
>>> status
{1: 1, 2: 2, 3: 3}
>>> type(status)
<class 'dict'>
