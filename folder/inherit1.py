# inherit

class Father:
    def eat(self):
        print('i haver a eat')
        pass

class Mother:
    def walk(self):
        print('i haver a walk ---')
        pass

class Son(Father,Mother):
        pass

s1 = Son()

if __name__ == "__main__":
    s1.eat()

if __name__ == "__main__":
    s1.walk()
