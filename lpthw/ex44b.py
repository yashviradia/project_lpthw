class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent() # Set dad to an instance of class Parent
son = Child() # Set son to an instance of class Child

dad.override() # from dad, get the function override with parameters self
son.override() # from son, get the function override with parameters self
