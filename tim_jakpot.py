import random
def player_name():
    while True:
        try:
            name = str(input("enter your name:."))
            int(input('enter phone number:.'))
            break

        except ValueError:
            print('invalid value')
            break
    print(f'welcome {name}')
    print('you can now play')
    return

player_name()

print("JAKPOT!!!")
print("TRY YOUR LUCKY!")
print('enter 3 numbers to try your lucky')
first = random.randrange(1, 5)
second = random.randrange(1, 5)
third = random.randrange(1, 5)
y = (first, second, third)

b = True
while b:
    try:
        x = int(input("enter your first luck number:"))
        a = int(input("enter your second luck number:"))
        s = int(input("enter your third luck number:"))
        break
    except ValueError:
        print('invalid value')

n = True
while n:
    if x and a and s in y:
        print("you won with a higher score your three numbers win")
        n = False
    elif x and s in y:
        print("you won with a moderate score your two numbers win")
        n = False
    elif x and a in y:
        print("you won with a moderate score your two numbers win")
        n = False
    elif a and s in y:
        print("you won with a moderate score your two numbers win")
        n = False
    elif x in y:
        print("you won with a less score your one number win")

        n = False
    elif a in y:
        print("you won with a less score your one number win")

        n = False
    elif s in y:
        print("you won with a less score your one number win")

        n = False

    else:
        print("try again, this may be your lucky time")

        n = False
print(f'you numbers {x},{a},{s} ')
print(f'lucky numbers {first},{second},{third}')
print('done')
input('press enter')