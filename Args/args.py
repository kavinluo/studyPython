# *args

# def add (pram1,pram2,pram3):
#     print(pram1+pram2+pram3)

# add(1,4,7)

# sum()自带求和

def add(*args):
    print(sum(args))

add(4,6,7)


def add1(*args):
        print(type(args))
        print(sum(args))
add1(1,4)