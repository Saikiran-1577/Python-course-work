Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#OutPut Formatting
a=10
b=23.5
>>> c="codegnan"
>>> a
10
>>> b
23.5
>>> c
'codegnan'
>>> print(a,b,c)
10 23.5 codegnan
>>> print('a=',a,'b=',b,'c=',c)
a= 10 b= 23.5 c= codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='')
a=10b=23.5c=codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
23.5
c=
codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	23.5	c=	codegnan
>>> print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n')
a=	10	b=	23.5	c=	codegnan

>>> print('a=',a,'b=',b,'c=',c,sep='\t',end='@')
a=	10	b=	23.5	c=	codegnan@
>>> print(f"a={a} b={b} c={c}")
a=10 b=23.5 c=codegnan
>>> print("a=%d b=%f c%s" %(a,b,c))
a=10 b=23.500000 ccodegnan
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=23.5 c=codegnan
>>> print('a={} b={} c={}'.format(b,c,a))
a=23.5 b=codegnan c=10
>>> print('a={2} b={1} c={0}'.format(a,b,c))
a=codegnan b=23.5 c=10
