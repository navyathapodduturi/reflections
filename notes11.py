Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f = open (testt.txt)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f = open (testt.txt)
NameError: name 'testt' is not defined
>>> pwd

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> cd ..
SyntaxError: invalid syntax
>>> cd

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    cd
NameError: name 'cd' is not defined
>>> f = open (notes.py)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    f = open (notes.py)
NameError: name 'notes' is not defined
>>> cwd

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cwd
NameError: name 'cwd' is not defined
>>> os.getcwd

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.getcwd
NameError: name 'os' is not defined
>>> getcwd

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    getcwd
NameError: name 'getcwd' is not defined
>>> 
>>> 


>>> 

>>> 


>>> 
>>> os.chdir

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    os.chdir
NameError: name 'os' is not defined
>>> NameError: name 'os' is not definedos.getcwd()
SyntaxError: invalid syntax
>>> getcwd()

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    getcwd()
NameError: name 'getcwd' is not defined
>>> os.getcwd()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> x = set()
>>> x
set([])
>>> x.add(1)
>>> x.add(787,998,876,0987)
SyntaxError: invalid token
>>> x.add(878)
>>> x
set([1, 878])
>>> i = [1,1,1,12,2,4,4,4,3,3,5}
SyntaxError: invalid syntax
>>> l = [1,1,1,1,2,2,4,4,5,3,3,3]
>>> x.add(l)

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x.add(l)
TypeError: unhashable type: 'list'
>>> a=set(l)
>>> a
set([1, 2, 3, 4, 5])
>>> set([1, 2, 3, 4, 5])
set([1, 2, 3, 4, 5])
>>> sqrt(()
     sqrt(9)
     
SyntaxError: invalid syntax
>>> 9**1/2
4
>>> 3**6
729
>>> 9**91/20
34279806620639876552680377474277002787691160631077838525800704585230711804364867108820L
>>> 9**(1/2)
1
>>> sqrt(9)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sqrt(9)
NameError: name 'sqrt' is not defined
>>> NameError: name 'sqrt' is not defined
SyntaxError: invalid syntax
>>> 4**0.5
2.0
>>> 2.0
2.0
>>> s='hello'
>>> s
'hello'
>>> s.index[-1]

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.index[-1]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> s.indesx

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s.indesx
AttributeError: 'str' object has no attribute 'indesx'
>>> s.index
<built-in method index of str object at 0x0303B4C0>
>>> s[:-1]
'hell'
>>> s[-1:]
'o'
>>> s[:-2]
'hel'
>>> s[-1::]
'o'
>>> s[-1::0]

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s[-1::0]
ValueError: slice step cannot be zero
>>> s[-1::1]
'o'
>>> l
[1, 1, 1, 1, 2, 2, 4, 4, 5, 3, 3, 3]
>>> l.sort
<built-in method sort of list object at 0x03047A30>
>>> e=set(l)
>>> e
set([1, 2, 3, 4, 5])
>>> 
