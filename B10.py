import math
def countDigit(n):
  return math.floor(math.log(n,10)+1)
n=34567890
print("number of digits: %d %(countDigit(n)))
