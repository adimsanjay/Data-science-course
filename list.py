Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#---list methods---
#pop,remove,sort,reverse
a=[10,20,30,55]
a
[10, 20, 30, 55]
help(a.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.

a.pop()
55
a
[10, 20, 30]
#by default pop()removes last element
#assignment:try -ve indexing
a.pop(-1)
30
a
[10, 20]
a.pop(-2)
10
a
[20]
#remove()method
help(a.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

a
[20]
b=[11,22,33,44,55]
b
[11, 22, 33, 44, 55]
b.remove(44)
b
[11, 22, 33, 55]
#pop()vsremove()
#pop is index base where remove is value base
#pop removes last element.remove()method removes first occurrence of specified element
#pop returns deleted value but in remove it return the direct o/p without showing deleted value
#========================================
#sort()
b
[11, 22, 33, 55]
c=[4,2,20,1,30,43,67]
c
[4, 2, 20, 1, 30, 43, 67]
c.sort()
c
[1, 2, 4, 20, 30, 43, 67]
c.reverse()
c
[67, 43, 30, 20, 4, 2, 1]
c.clear()
c
[]
d=[2,45,67,90,3,2]
d
[2, 45, 67, 90, 3, 2]
#if want this list in descending order using sort() method
d.sort(reverse=True)
d
[90, 67, 45, 3, 2, 2]
