a=float(input("Enter the value:"))
b=float(input("Enter the value:"))
print("operations")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.modulus")
print("6.greater")
print("7.lesser")
ch =int(input("Enter your choice:"))
if ch == 1 :
  print ("Addition :",a+b)
elif ch == 2 :
  print ("Subtraction:",a-b)
elif ch ==3 :
  print ("Multiplication:",a*b)
elif ch ==4 :
  print ("Division:",a/b)
elif ch ==5 :
  print ("Modulus:",a%b)
elif ch == 6 :
  print ("Greater than :",a>b)
elif ch ==7 :
  print ("Lessthan :",a<b)
else: 
  print ("Error..!!!")
