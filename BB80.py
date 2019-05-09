l=[]
n=int(input("enter how many number:"))
for i in range(n):
num=int(input("enter the number:"))
l.append(num)
for x in l:
if(x%2!=0):
print(x)
