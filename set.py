Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#**********Set***********
#-----Features of set------
#1.Background ds is Hash table
#2.set doesn't allow duplicates
#3.it doesn't preserve sequence bz of hash table
#4.Its not like array so we dont have indexing n slicing
#5.it is mutable
#6.it allows homo/hetro values
#set syntax:
a={6,10.2,'A'}
a
{10.2, 6, 'A'}
#---Set methods---
a.add(20)
a
{10.2, 20, 6, 'A'}
#pop,remove,discard()
a.pop()
10.2
a
{20, 6, 'A'}
help(set.pop)
Help on method_descriptor:

pop(...)
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.

a.remove()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.remove()
TypeError: set.remove() takes exactly one argument (0 given)
a.remove(6)
a
{20, 'A'}
#here we can see pop() method dont need value but i  remove method must have value
a.discard(20)
a
{'A'}
help(set.discard)
Help on method_descriptor:

discard(...)
    Remove an element from a set if it is a member.
    
    If the element is not a member, do nothing.

#it means it takes exactly one arg n suppose write something diff from set then it will not give error means it do nothing
    
a.discard('aditi)
          
SyntaxError: unterminated string literal (detected at line 1)
a.discard('aditi')
         
a        
{'A'}

          
