Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_list = ['string',1.23,2345,876]
>>> my_list
['string', 1.23, 2345, 876]
>>> my_list[0]
'string'
>>> my_list+ 'add strut'

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    my_list+ 'add strut'
TypeError: can only concatenate list (not "str") to list
>>> my_list+['add strut']
['string', 1.23, 2345, 876, 'add strut']
>>> my_list.
SyntaxError: invalid syntax
>>> my_list.pop(-1)
876
>>> l_1 = [1,2,3]
>>> l_2 = [4,5,6]
>>> l_3 = [7,8,9]
>>> matrix = [l_1,l_2,l_3]
>>> matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> matrix[2][3]

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    matrix[2][3]
IndexError: list index out of range
>>> matrix[2][2]
9
>>> my_dict ={'k1'=123,'k2'=34.56,'k3'= 7898}
SyntaxError: invalid syntax
>>> my_dict ={'k1':123,'k2':34.56,'k3': 7898}
>>> my_dict
{'k3': 7898, 'k2': 34.56, 'k1': 123}
>>> {'k3': 7898, 'k2': 34.56, 'k1': 123}my_dict['k3']
SyntaxError: invalid syntax
>>> my_dict['k3']
7898
>>> my_dict
