print("JAKPOT!!!")
print("TRY YOUR LUCKY!")
import random

y=random.randrange(1,100)
n= True

while n:
  try:
    x = float(input("enter you luck number:"))
    if  x in y  :
      print("you won")
      n= False
    else:
      print("try again, this may be your lucky time")
  except:
    print('Please enter a number')
