Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#------------String methods------------
a='good Morning'
a
'good Morning'
a.count('o')
3
a.count(' ')
1
a.count('n')
2
a.startswith('g')
True
a.endswith('g')
True
a.find('o')
1
a.find('n')
8
a.find('Morning')
5
enumerate(a)
<enumerate object at 0x00000204B0CC8280>
list(enumerate(a))
[(0, 'g'), (1, 'o'), (2, 'o'), (3, 'd'), (4, ' '), (5, 'M'), (6, 'o'), (7, 'r'), (8, 'n'), (9, 'i'), (10, 'n'), (11, 'g')]
a.index('M')
5
a.casefold()
'good morning'
#casefold means where all the chara convert in lower case
#----find vs index------
a.find('MM')
-1
a.index('MM')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.index('MM')
ValueError: substring not found
a.split()
['good', 'Morning']
b=['Rakesh','Gaikwad']
b
['Rakesh', 'Gaikwad']
#if want to get list of str use join method
' '.join(b)
'Rakesh Gaikwad'
'-'.join(b)
'Rakesh-Gaikwad'
#*******is methods in str*******
'123'.isdigit()
True
'aditi'.isalpha()
True
'aditi123'.isalnum()
True
'010101'.isascii()
True
'200'.isdecimal()
True
'0.4'.isdecimal()
False
'Aditi'.islower()
False
'sky'.isprintable()
True
m="Hello"
c=m.isidentifier()
print(c)
True
#it check valid identifier(a-z,0-9,_)but not start with no or any spaces
a
'good Morning'
print(a.isidentifier())
False
n='aditi'
print(n.isidentifier())
True
a.format()
'good Morning'
x="aditi {mname} Mahadar".format(mname="Sanjay")

x
'aditi Sanjay Mahadar'
#format method add chara using dict
x.replace('aditi','Tejas')
'Tejas Sanjay Mahadar'
