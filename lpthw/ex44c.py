class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered() # call "super" with arguments "Child" and "self", then call the function "altered" on whatever it returns
        print("CHILD, AFTER PARENT altered()")

dad = Parent() # Set dad to an instance of class Parent
son = Child() # Set son to an instance of class Child

dad.altered() # from dad, get the function altered with the parameters self
son.altered() # from son, get the function altered with the parameters self
