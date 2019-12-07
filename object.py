
# this is my python program

class Student:
    name ='kevin'
    age = 18
    def eat(self):
        print('yes', self.name, 'can eat!')
    def cat(self):
        print('this is my cat',self.age)
        print(self.eat())

    @staticmethod
    def wok():
        print('work')

xiaom = Student()
xiaom.eat()
xiaom.cat()
xiaom.wok()

