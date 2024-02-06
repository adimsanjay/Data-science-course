Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#--------typecasting---------
#--------explicit typecasting--------
int(40/2)
20
float(20*10)
200.0
#-------implicit typecasting---------
10+20+30
60
10+20.+30
60.0
#int->float->complex
#--------String---------
m='Aditi Mahadar'
m
'Aditi Mahadar'
len(m)
13
m[:5]
'Aditi'
m[5:]
' Mahadar'
m[:6]
'Aditi '
m[6:]
'Mahadar'
m[-3:]
'dar'
m[-1:-3:-1]
'ra'
m[-1:-4:-1]
'rad'
m
'Aditi Mahadar'
m[:5]
'Aditi'
m[:5][::-1]
'itidA'
m[:7]
'Aditi M'
m[7:]
'ahadar'
m[6:]
'Mahadar'
m[:5:-1]
'radahaM'
