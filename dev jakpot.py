

print("JAKPOT!!!")
print("TRY YOUR LUCKY!")
import random
first=random.randrange(1, 100)
second=random.randrange(1, 100)

third=random.randrange(1, 100)
b=True
while b:
     try:
         x = int(input("enter your first luck number:"))
         b=False
     except:
         print('please enter number instead!')
n=True
while n:
     try:
       a = int(input("enter your second luck number:"))
       n=False
     except:
       print('please enter number instead!')
n = True
while n:
     try:
       s = int(input("enter your third luck number:"))
       n = False
     except:
         print('please enter number instead!')
n = True
while n:
     if  x==first and a==second and s==third:
            print("you won with a higher score your three numbers win")
            n= False
     elif x==first and s==third:
            print("you won with a moderate score your two numbers win")
            n= False
     elif x==first and a==second:
            print("you won with a moderate score your two numbers win")
            n= False
     elif a==second and s==third:
            print("you won with a moderate score your two numbers win")
            n= False
     elif x==first:
            print("you won with a less score your one number win")
        
            n= False
     elif a==second:
            print("you won with a less score your one number win")
        
            n= False
     elif  s==third:
            print("you won with a less score your one number win")
        
            n= False            
        
     else:
            print("try again, this may be your lucky time")
            n=False
print(f'you numbers {x},{a},{s} ')
print( f'lucky numbers {first},{second},{third}')
input('done press enter ')