import random

while True:
    com=random.randint(1,3)
    print("1. scissors")
    print("2. rock")
    print("3. paper")
    me=int(input("code : "))
    print("me : %d, com : %d"%(me,com))
    if com==1:
        if me==1:
            print("draw")
        elif me==2:
            print("win")
        elif me==3:
            print("lose")
        else:
            print("Choose one out of 1 2 3")
    elif com==2:
        if me==1:
            print("lose")
        elif me==2:
            print("draw")
        elif me==3:
            print("win")
        else:
            print("Choose one out of 1 2 3")
    elif com==3:
        if me==1:
            print("win")
        elif me==2:
            print("lose")
        elif me==3:
            print("draw")
        else:
            print("Choose one out of 1 2 3")