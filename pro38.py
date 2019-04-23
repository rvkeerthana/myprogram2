x=int(input("enter any number\n"))
print("this factor of,"x",are:")
for i in range(1,x+1):
if x%i==0:
if i%2==0:
print(i,"even")
else:
print(i,"odd")
