class Students:
      def __init__(self,name,age):
            self.name = name
            self.age = age

      def walk(self):
          print(self.name,'today is old',self.age)


sle = Students('kevin',33)
sle.walk()

s2 = Students('james', 32)
s2.walk()

