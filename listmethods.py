Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#-------LIST-------
#-----features of list--------1.list is mutable,2.Background ds is array,3.it contains duplicate records,4.+ve & -ve indexing supported,5.slicing also possible,6.it preserves sequence order
#lets see eg
a=[10,20,30,40,50,60]
a
[10, 20, 30, 40, 50, 60]
a[4]
50
a[-3]
40
#--it support
#+ve n -ve indexing
a[:]
[10, 20, 30, 40, 50, 60]
#slicing
a[::-1]
[60, 50, 40, 30, 20, 10]
a[-4::-1]
[30, 20, 10]
a[-4::1]
[30, 40, 50, 60]
b=[10,10,20,30,30,40]
b
[10, 10, 20, 30, 30, 40]
#using append()method we can add str in list
b.append('abc')
b
[10, 10, 20, 30, 30, 40, 'abc']
#append() adds whole object where extend()adds elements from an iterable
b.extend('aditi')
b
[10, 10, 20, 30, 30, 40, 'abc', 'a', 'd', 'i', 't', 'i']
#int obj is not iterable
b.extend('100')
b
[10, 10, 20, 30, 30, 40, 'abc', 'a', 'd', 'i', 't', 'i', '1', '0', '0']
b.extend(100)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b.extend(100)
TypeError: 'int' object is not iterable
b.clear()#it removes all items from list
b
[]
#Shallow copy & Deep copy
#Shallow copy means it copy the content n create new obj
c1=[1,2,3,4]
c1
[1, 2, 3, 4]
c2=c1.copy()
c2
[1, 2, 3, 4]
#but address of c1 n c2 will be diff
#Deep copy means copy contents,address will same but not create new obj
c2
[1, 2, 3, 4]
c3=c2
c3
[1, 2, 3, 4]
c3.append(5)
c3
[1, 2, 3, 4, 5]
c2
[1, 2, 3, 4, 5]
#insert():add element at specific index
c2
[1, 2, 3, 4, 5]
c2.insert(4,'aditi')
c2
[1, 2, 3, 4, 'aditi', 5]
#assignment
e1=[10,20,30,40]
e1
[10, 20, 30, 40]
#add java before 10
e1.insert(0,'java')
e1
['java', 10, 20, 30, 40]
#add ur name after 50
#*40
e1.insert('aditi')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    e1.insert('aditi')
TypeError: insert expected 2 arguments, got 1
e1.insert(40,'aditi')
e1
['java', 10, 20, 30, 40, 'aditi']
e1.append('aditi')
e1
['java', 10, 20, 30, 40, 'aditi', 'aditi']
