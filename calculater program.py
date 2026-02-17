num1 = float(input("enter first number:"))
num2 =float(input("enter secand number:"))
operator = input("enter operator(+,-,*,/):")
if operator == '+':
  result =num1+num2
  print(f"result={result}")
elif operator=='-':
  result=num1-num2
  print(f"result={result}")
elif operator =='*':
  result=num1*num2
  print(f"result={result}")
elif operator=='/':
  if num2 ==0:
    print('error:division by zero')
  else:
    result=num1/num2
    print(f"result={result}")
else:
  print("invalid operator")
