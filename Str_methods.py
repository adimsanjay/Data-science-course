Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#----------String methods-----------
#''.=it will display list of str methods
name='Aditi Sanjay Mahadar'
name
'Aditi Sanjay Mahadar'
name.split()
['Aditi', 'Sanjay', 'Mahadar']
name.upper()
'ADITI SANJAY MAHADAR'
name.lower()
'aditi sanjay mahadar'
name.capitalize()
'Aditi sanjay mahadar'
name.title()
'Aditi Sanjay Mahadar'
#convert upper to lower and lower to upper following word
x='ADitI'
x
'ADitI'
x.swapcase()
'adITi'
name
'Aditi Sanjay Mahadar'
name.replace('Aditi','Amruta')
'Amruta Sanjay Mahadar'
a='  Aditi   '
a
'  Aditi   '
a.strip()
'Aditi'
a.replace(' ','')
'Aditi'
#-------Remove # and * using replace
nm='#Aditi#'
nm.replace('#')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    nm.replace('#')
TypeError: replace expected at least 2 arguments, got 1
nm.replace('#','*')
'*Aditi*'
