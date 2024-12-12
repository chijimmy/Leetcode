class Dog:

    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
        
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

class puppy(Dog):
    def __init__(self, name, classification,size):
        
        self.size=size
        self.classification=classification
        Dog.__init__(self,name)
    
    def details(self):
        print("My dog is {}".format(self.name))
        print("classification: {}".format(self.classification))
        print("Size: {}".format(self.size))

a = puppy('Rahul', "French Bulldog", 14)

a.display()
a.details()