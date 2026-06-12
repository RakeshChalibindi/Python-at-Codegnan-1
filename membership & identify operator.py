Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#membership operator

a=[1,2,3,4,5]
print(1 in a)
True
>>> print(7 in a)
False
>>> print(10 not in a)
True
>>> b=[10,20,30,45]
>>> print(10 in b)
True
>>> #identify operator
>>> 
>>> A=[1,2,3,4,5]
>>> print(a)
[1, 2, 3, 4, 5]
>>> print(1 is a)
False
>>> a=[1,2,3,4]
>>> b=a
>>> c=[33,4,5,6]
>>> print(a is b)
True
>>> print(a is c)
False
>>> print(a is not c)
True
>>> c=[2,4,5,6,7,9]
>>> print(c is not b)
True
>>> a=[10,23.4,66]
>>> b=a
>>> c=[34,56,77]
>>> print(c is a)
False
