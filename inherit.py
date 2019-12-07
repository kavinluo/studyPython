# inherit

class Father:
    def eat(self):
        print('i haver a eat')

class Mother:
    def walk(self):
        print('i haver a walk ')

class Son(Father,Mother):
    pass

s1 = Son()

s1.eat()
s1.walk()