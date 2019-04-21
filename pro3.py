number=int(input("please enter any number:"))
revverse=0
while(number>0):
reminder=number%10
reverse=(reverse*10)+reminder
number=number//10
print("reverse of number=%d"%reverse)
