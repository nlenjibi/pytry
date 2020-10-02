

x= input("enter your first name: ")
a=input("enter your second name: ")
n=True
while n:
 try:
  c= float(input("enter your age: "))
  if c == 25:
    print("you are welcome "+ x +" " + a +"!")
    print("you are qualified for the position")
    n=False
  elif c> 25:
    print("the age limit is lower than what you entered!")
  else:
    print("the age limit is greater what you entered!")
 except:
    print('Please enter a number')

 
print(input('done press enter'))