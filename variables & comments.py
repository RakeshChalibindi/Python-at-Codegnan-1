Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1,num2,num3 = 10,20,30
>>> print(num1)
10
>>> print(num2)
20
>>> print(num3)
30
>>> print("hello world")
hello world
>>> num1=num2=num3=10
>>> print(num1)
10
>>> print(num2,num3)
10 10
>>> print(id(num2))
140731239171272
>>> print(id(num1))
140731239171272
>>> a,b=20,40
>>> print(id(a),id(b))
140731239171592 140731239172232
>>> a,b=256,256
>>> print(id(a),id(b))
140731239179144 140731239179144
>>> 140731239179144 140731239179144
SyntaxError: invalid syntax
>>> a=10
>>> b=20
>>> a,b=b,a
>>> print(a)
20
print(b)
10
print(id(a),id(b))
140731239171592 140731239171272
