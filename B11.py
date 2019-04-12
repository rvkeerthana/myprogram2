def check_Power(N,k):
  if N<= 0 or k<=0:
     print("not a vaild input")
  else:
     for i in range(1,20):
         x=k**i
         if x==N:
            print("true")
            print(k."power",i,"is",N)
            break
         else x>N:
            print("false")
            break
check_power(2223445567,5)
check_Power(4096,16)
check_Power(0,16)
check_Power(1,1)
