Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#=======Set Operations=======
s1={'w','x','y','z'}
s1
{'x', 'y', 'w', 'z'}
#intersection():it returns common elements
s2={'X','A','B','Y','C'}
s2
{'C', 'B', 'X', 'Y', 'A'}
s1.intersection(s2)
set()
s3={'A','N','C','y','z'}
s3
{'C', 'z', 'y', 'A', 'N'}
s2.intersection(s3)
{'C', 'A'}
#union():returns all elements from both set without duplicates
s2.union(s3)
{'C', 'X', 'N', 'B', 'z', 'Y', 'y', 'A'}
#difference():returns uncommon elements
s2.difference(s3)
{'B', 'X', 'Y'}
#Symmetric difference():returns uncommon elements from both set
s2.symmetric_difference(s3)
{'B', 'X', 'z', 'Y', 'y', 'N'}
#Assignment:
#update()method:
help(s1.update)
Help on built-in function update:

update(...) method of builtins.set instance
    Update a set with the union of itself and others.

s1.update(s2)
s1
{'x', 'C', 'X', 'B', 'z', 'Y', 'y', 'w', 'A'}
s2.update(s3)
s2
{'C', 'X', 'N', 'B', 'z', 'Y', 'y', 'A'}
#it upxdate the current set by adding items from another set
#---------------------
#difference_update():
m1={1,2,3,4,5,6}
m1
{1, 2, 3, 4, 5, 6}
m2={10,20,30,40,50}
m2
{50, 20, 40, 10, 30}
m1.difference_update(m2)
m1
{1, 2, 3, 4, 5, 6}
m3={10,4,2,3,20,30,40}
m3
{2, 3, 4, 20, 40, 10, 30}
m2.difference_update(m3)
m2
{50}
#it removes the items that exist in both set
#so diff between=difference()method return new set without removing unwanted items and difference_update removes unwanted items from original set
#----------------------
#symmetric_difference_update():
n1=
SyntaxError: invalid syntax
n1={'Mango','Apple','Banana','Strawberry'}
n1
{'Mango', 'Banana', 'Apple', 'Strawberry'}
help(n1.symmetric_difference_update)
Help on built-in function symmetric_difference_update:

symmetric_difference_update(...) method of builtins.set instance
    Update a set with the symmetric difference of itself and another.

n2={'Blueberry','Kiwi','Mango','Apple','Banana'}
n2
{'Blueberry', 'Banana', 'Kiwi', 'Mango', 'Apple'}
n1.symmetric_difference_update(n2)
n1
{'Strawberry', 'Kiwi', 'Blueberry'}
#it removes duplicates from both set
#------------------------
#intersection_update():
b1={'c','d','e','f','g'}
b1
{'g', 'f', 'e', 'c', 'd'}
b2={'x','d','y','f','z'}
b2
{'x', 'f', 'z', 'y', 'd'}
help(b1.intersection_update)
Help on built-in function intersection_update:

intersection_update(...) method of builtins.set instance
    Update a set with the intersection of itself and another.

b1.intersection_update(b2)
b1
{'f', 'd'}
#it returns duplicate values from both set 