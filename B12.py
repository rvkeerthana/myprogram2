num=input("enter any number:")
try:
   val = int(num)
   if num==str(num)[::-1]:
      print("the given number is palindrome")
   else:
      print("the given number is not a palindrome")
except ValueError:
  print("this is not a valid number,try again!")
