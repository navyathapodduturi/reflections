Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l = [13,34,55,65,7,567,897,6545]
>>> for num in l:
	if num % 2 == 0:
		 print 'even'
		  elif num % 2 != 0:
			  
  File "<pyshell#4>", line 5
    elif num % 2 != 0:
    ^
IndentationError: unexpected indent
>>> for num in l:
	if num % 2 == 0:
		print 'even'

		
even
>>> for num in l:
	if num % 2 == 0:
		print 'even'
		 else:
			 
  File "<pyshell#10>", line 5
    else:
    ^
IndentationError: unexpected indent
>>> for num in l:
	if num % 2 == 0:
		print 'even'
		else:
			
SyntaxError: invalid syntax
>>> 
