import sys
sys.path.append('../app2') # add the pathh of the parent folder 
from package1 import Person
from package2 import add,sub
from sub_app.package3 import Car, Animal
from package5 import Laptop,hello
from package6 import Student,NAME

person = Person()

add(3,4)
bmw = Car()
hp = Laptop()
hello()
print(NAME)

