Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string operations continue
>>> '213456'isdecimal()
SyntaxError: invalid syntax
>>> '213456'.isdecimal()
True
>>> 'UIHSUBSBVIUEB'.isdecimal
<built-in method isdecimal of str object at 0x000001F751E04270>
>>> 'UIHSUBSBVIUEB'.isdecimal()
False
>>> 'SAIKIRaN'.istitle()
False
>>> '9877654'.isnumeric()
True
>>> '9807'.isnumeric()
True
>>> '43534'.isdecimal()
True
>>> s = "    Hello World  "
>>> s.strip()
'Hello World'
>>> s.lstrip()
'Hello World  '
