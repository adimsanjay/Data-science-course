'''
---------Pattern programs---------
1) *
   * *
   * * *
   * * * *
   * * * * *
for i in range(1,6):
    print(i * ' * ')
----------------------------------
2) * * * * *
   * * * *
   * * *
   * *
   *
for i in range(5,0,-1):
    print( i *  ' * ' )
---------------------------------
3) * * * * *
   * * * * *
   * * * * *
   * * * * *
for i in range(0,4):
    print(' * ' * 4)
----------------------------------
4) 1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end= ' ')
    print()
-----------------------------------
5)A
  A B
  A B C
  A B C D
  A B C D E
for i in range(1,6):
    for j in range(i):
        print(chr(65 + j),end=' ')# ascii value of A
    print()
-------------------------------------
6)A
  B C
  D E F
  G H I J
  K L M N O
ascii_value = 65
for i in range(1,6):
    for j in range(i):
        print(chr(ascii_value),end=' ')
        ascii_value += 1
    print()
---------------------------------------
7) 1
   2 3
   4 5 6
   7 8 9 10
num = 1
for i in range(1,5):
    for j in range(i):
        print(num,end=' ')
        num += 1
    print()
--------------------------------------
8) dddd
    ccc
     bb
      a
for i in range(4,0,-1):
    print(' ' * (4-i)  + chr(96+i)*i)
---------------------------------------
9) dddd
   ccc
   bb
   a
for i in range(4):
    for j in range(4-i):
        print(chr(100 - i), end='')
    print()
'''










