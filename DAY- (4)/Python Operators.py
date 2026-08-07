Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python operators
'''
1.Arthemetical
2.Comparision
3.Assignment
4.Relation
5.Membership
6.Identity
7.Bit wise
'''
'\n1.Arthemetical\n2.Comparision\n3.Assignment\n4.Relation\n5.Membership\n6.Identity\n7.Bit wise\n'
a= 10
b= 5
a+b
15
a_b
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a_b
NameError: name 'a_b' is not defined
a-b
5
a*b
50
a/2
5.0
9/2
4.5
9//2
4
10.2//2
5.0
a**2
100
16**2
256
12%2
0
#comparision operator
a
10
b
5
a>b
True
a<b
False
a>=b
True
a<=b
False
a==b
False
a!=b
True
#assignment
a=20
a=a


a=a+20

a
40
a+=10
a
50
a -=10
a
40
a*=20
a
800
a //=2
a
400
a **= 2
a
160000
a %=2
a
0
a +=2
a
2
a
2
a +=48
a
50
#Relational
email = True
password = False
email and password
False
login = True
login = False
display_products = True
login or dispaly
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    login or dispaly
NameError: name 'dispaly' is not defined
login or display_products
True
's' in 'aeiou'
False
's' not in 'aeiou'
True
7%2==0 and 3%2==0
False
2%2==0 and 3%2==0
False
6%2==0 or 3%2==0
True
3%2==0
False
not 7%2==0 and 3%2==0
False
not 7%2==0
True
#Membership
#str list tuple set dict
s = 'python programming'
'python' in s
True
'java' in s
False
'z' in s
False
'c++'not in s
True
"python" not in s
False
l = [1,2,3,4,5]
3 in l
True
9 not in l
True
9 in l
False
1 not in l
False
1 in l
True
t = (40,50,60,70)
70 in t
True
90 not in t
True
70 not in t
False
s = {'black', 'blue','pink'}
black in s
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    black in s
NameError: name 'black' is not defined
'black' in s
True
' blue ' not in s
True
'pink' in s
True
d = {'name':'sai','Dob':'2006','course':'PFS'}
d
{'name': 'sai', 'Dob': '2006', 'course': 'PFS'}
'name' in s
False
'name' in d
True
'name' not in d
False
'sai' in d
False
'sai' not in d
True
'course' in d
True
#Indentity

l=[1,2,3,4]
m=[1,2,3,4]
id(l)
1906428807168
id(m)
1906428724864
l is m
False
m is l
False
l is not m
True
m == n
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    m == n
NameError: name 'n' is not defined
n=m
n
[1, 2, 3, 4]
id(n)
1906428724864
>>> m is n
True
>>> n is m
True
>>> n is l
False
>>> l is n
False
>>> n is not true
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    n is not true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> n is not l
True
>>> #BitWise
>>> 11 & 12
8
>>> 11 | 12
15
>>> 2<<2
8
>>> 2<<3
16
>>> 2<<4
32
>>> 16>>2
4
>>> ~14
-15
>>> ~18
-19
>>> 5>>7
0
>>> 8<<5
256
