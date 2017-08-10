Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n = 0
>>> while n<10:
	print 'hello is-',n
	n += 1
	if n == 3:
		print 'its done'

		
hello is- 0
hello is- 1
hello is- 2
its done
hello is- 3
hello is- 4
hello is- 5
hello is- 6
hello is- 7
hello is- 8
hello is- 9
>>> while n<10:
	print 'hello',n
	n += 1
	if n == 3:
		break

	
>>> 
>>> n = 0
>>> while n<10:
	print 'hello',n
	n += 1
	if n == 3:
		break

	
hello 0
hello 1
hello 2
>>> 
>>> x = range(5,15)
>>> 
>>> x
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> lst = [num for num in range(0,25) if num % 2 ==0]
>>> lst
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
>>> 
