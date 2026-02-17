name =input("Enter student nmae:")
mark1=float (input("Enter mark1(1-100):"))
mark2=float(input("Enter mark2(1-100):"))
mark3=float(input("Enter marks1(1-100):"))
total=mark1+mark2+mark3
percentage=(total/300)*100
print(f"\n{name}")
print(f"total:{int(total)}/300")
print(f"percentage:{percentage:.1f}%")
if percentage>75:
  print("Grade:A")
elif percentage>=60:
  print("Grade:B")
elif percentage>=40:
  print("Grade:c")
else:
  print("Grade:F")