str=input("enter the string:")
try:
i=float(str)
except(ValueError,TypeError):
print('\nNot numeric')
print()
