class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER override()")

    def altered(self):
        print("OTHER override()")

class Child(Other):

    def __init__(self):
        self.other = Other()

    def override(self):
        print("CHILD override()")

    def implicit(self):
        self.other.implicit()

    def altered(self):
        print("CHILD, BEFORE altered()")
        super(Child, self).altered()
        print("CHILD, AFTER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
