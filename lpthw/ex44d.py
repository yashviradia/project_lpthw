class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

#    def implicit(self):
#        pass

    def altered(self):
        print("CHILD, BEFORE PARENT override()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT override()")

dad = Parent() # Set 'dad' to an instance of the class 'Parent'
son = Child() # Set 'son' to an instance of the class 'Child'

dad.implicit() # From 'dad', get the function 'implicit' with parameters 'self'
son.implicit() # From 'son', get the function 'implicit' with parameters 'self'

dad.override() # From 'dad', get the function 'override' with parameters 'self'
son.override() # From 'son', get the function 'override' with parameters 'self'

dad.altered() # From 'dad', get the function 'altered' with parameters 'self'
son.altered() # From 'son', get the function 'altered' with parameters 'self' 
