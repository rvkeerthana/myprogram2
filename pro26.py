import re
text1='python             exercise'
print("original string:",text1)
print("without extra space:",re.sub('+','',text1))
