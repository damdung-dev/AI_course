from POO21 import Students


class Person:
    count=0

    def __init__(self, name, age):
        self.__name=name
        self.__age=age
        Person.increment_count(self)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.getter
    def age(self, age):
        self.__age = age
    def increment_count(self):
        Person.count+=1
    def greeting(self):
        print("Hello!")
    def cls_information(self):
        print("")
    def __str__(self):'''