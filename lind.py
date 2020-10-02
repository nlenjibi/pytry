n = True
while n:
 try:
  tim = float(input('enter your first number:'))
  n= False
 except:
  print('please enter a number instead!')
con = input('enter your operator:')
n= True
while n:
 try:

  vim = float(input('enter your second number:'))
  n=False
 except:
    print('please enter a number instead!')
if con=='+':
    print( tim + vim)
elif con=='-':
    print(tim - vim)
elif con=='*':
    print(tim * vim)
elif con=='/':
    print(tim / vim)
elif con=='>':
    if tim>vim:
     print('True')
    else:
     print('False')
elif con=='<':
    if tim<vim:
        print("True")
    else:
        print('False')

elif con=='^':
    print(tim ** vim)

else:
    print('invalid operator')
print('done')
input('press enter!')