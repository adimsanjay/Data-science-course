'''
#1)how to count no of occurrences of any specific characters in string using loop
string = "aaaaaaaabbbbbddddd"
char_count = "a"
count = 0
for c in string:
    if c == char_count:
        count += 1
print("no of occurrences of " + char_count + " are: ",count)
--------------------------------------------------
#2)Find all the vowels from given string using for loop
string = "Hi my name is imran"
vowels = "aeiou"
find_vowels = []

for char in string:
    if char in vowels:
        find_vowels.append(char)
print("Vowels found in the string: ",find_vowels)
-------------------------------------------------
#3).Want to capitalize string using for loop
string = "hi i am aditi"
capitalize_string= ""
#split sentence into words
words = string.split()
for word in words:
     capitalize_word=word.capitalize()
     capitalize_string += capitalize_word + " "
print("Original string is:", string)
print("capitalize string is:",capitalize_string)
--------------------------------------------
#4)find out n display code separately
a = "hello i am sending this two codes to u is 43567 and 27388"
for num in a.split():
    if num.isdigit():
        print(num)
-------------------------------------------------
#5)write a program to replace spaces with special chara in given string in python
string = "  hello  world  "
replace_char = "-"
result = string.replace(" ", replace_char)

print("Original string:", string)
print("After replacement:", result)
'''
#6)Find any character in str
string = "aditi"
character = "t"

index = string.find(character)
if index != -1:
    print("chara of " + string + "found at index:" ,index)
else:
    print("chara not found",character)



