class Parent(object):

    def altered(self):
        print("PARENT altered()")

    
class Child(Parent):

    def altered(self):
        print("CHILD  BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD  AFTER altered()")


# >>> from ex44c import *
# >>> dad = Parent()
# >>> son = Child()
# >>> dad.altered()
# PARENT altered()
# >>> son.altered()
# CHILD  BEFORE PARENT altered()
# PARENT altered()
# CHILD  BEFORE AFTER altered()
# >>>