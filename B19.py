def factorial(n):
if n==0:
return 1
else:
return n * factorial(n-1)
n=int(input("input a number to complete the factorial: "))
print(factorial(n))
