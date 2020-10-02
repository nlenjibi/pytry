print('logical calculator)
n=True
while n:
 try:
  x = float(input("enter your first number: "))
  n=False
 except: 
    print("enter a number intead!")
    
a = input("enter the operator: ")
b=True
while b:
 try:
   y =float( input("enter your second number: "))
   b=False
 except:
    print("enter a number intead!")
if a == "+":
    print(x + y)
elif a == "*":
    print(x * y)
elif a == "-":  
    print(x - y)
elif a == "/":
    print( x / y)
    
elif a == ">":
      if x > y:
        print("true")
      else:
        print("false")
elif a== "<":
 if x < y:
  print("true")
 else:
  print("false")

elif a== "^":
  print (pow(x,y))
else:
    print("invalid operator")
print(input("done press enter"))