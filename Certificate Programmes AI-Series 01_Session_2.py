Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> square = [1,4,9,25]
>>> square
[1, 4, 9, 25]
>>> square[0]
1
>>> square[10]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    square[10]
IndexError: list index out of range
>>> square[-1]
25
>>> square[|:2]
SyntaxError: invalid syntax
>>> square[:2]
[1, 4]
>>> square[:]
[1, 4, 9, 25]
>>> square[2:]
[9, 25]
>>> square[-3:]
[4, 9, 25]
>>> square
[1, 4, 9, 25]
>>> square + [36,49,64]
[1, 4, 9, 25, 36, 49, 64]
>>> new_list = square + [36,49,64]
>>> new_list
[1, 4, 9, 25, 36, 49, 64]
>>> r ="hello!"
>>> r[2]
'l'
>>> new_list[2]=10
>>> new_list
[1, 4, 10, 25, 36, 49, 64]
>>> new_list.append(81,100)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    new_list.append(81,100)
TypeError: list.append() takes exactly one argument (2 given)
>>> new_list.append(81)
>>> new_list
[1, 4, 10, 25, 36, 49, 64, 81]
>>> new_list.insert(2,100)
>>> new_list
[1, 4, 100, 10, 25, 36, 49, 64, 81]
>>> 
>>> 
>>> 
>>> letters = ['a','b','c','d','e','f','g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5]=['C','D','E']
>>> LETTERS
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    LETTERS
NameError: name 'LETTERS' is not defined
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> letters = []
>>> letters
[]
>>> letters = ['a','b','c','d','e','f','g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> len(letters)
7
>>> a =['a','b','c']
>>> n = [1,2,3]
>>> c =a+n
>>> c
['a', 'b', 'c', 1, 2, 3]
>>> x = (a,n)
>>> x
(['a', 'b', 'c'], [1, 2, 3])
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>> age = int(input())
20
>>> age
20
>>> name = input()
Bobby
>>> age = input()
10
>>> print("Name : " + name + '/n Age : ' + age)
Name : Bobby/n Age : 10
>>> print("Name : " + name + /n + 'Age : ' + age)
SyntaxError: invalid syntax
>>> print("Name : " + name + '\n Age : ' + age)
Name : Bobby
 Age : 10
>>> 
>>> 
>>> # Conditional Clauses
>>> 
>>> 
>>> q =4
>>> if 