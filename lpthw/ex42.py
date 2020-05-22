## Animal is-a object (yes, sort of confusing) look at the example
class Animal(object):
    pass

## Dog is-a Animal, Make a class named Dog that is-a Animal
# Class Dog has-a __init__ with parameters self and name
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal, Make a class named Cat that is-a Animal
# Class Cat has-a __init__ with parameters self and name
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object, Make a class named Person that is-a object
# Class Person has-a __init__ with parameters self and name
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person, Make a class named Employee that is-a Person
# class Employee has-a __init__ with parameters self, name, salary
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? it temporary allows you to call the object and then giving you power to call method
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object, Make a class named Fish that is-a object
class Fish(object):
    pass

## Salmon is-a Fish, Make a class named Salmon that is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish, Make a class named Halibut that is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog and has-a name Rover
rover = Dog("Rover")

## satan is-a Cat and has-a name Satan
satan = Cat("Satan")

## mary is-a Person and has-a name Mary
mary = Person("Mary")

## mary has-a pet who has-a name satan, From mary, get the attribute pet, and set it to rover
mary.pet = satan

## frank is-a Employee who has-a name Frank and salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet who has-a name rover, From frank, set the attribute pet, and set it to rover
frank.pet = rover

## flipper is-a Fish, Set flipper to an instance of class Fish
flipper = Fish()

## crouse is-a Salmon, Set crouse to an instance of class Salmon
crouse = Salmon()

## harry is-a Halibut, Set harry to an instance of class Halibut
harry = Halibut()
