def rem_vowel (string):
vowels=('a','e','i','o','u')
for x in string.lower():
if x in vowels:
string=string.replace(x, "")
print(string)
string=input("enter the word:")
rem_vowel(string)
